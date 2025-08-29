from scipy.sparse import csr_matrix, hstack, save_npz, load_npz


import numpy as np
import csv
import os
import pandas as pd

num_champions = 171


def _load_csv(path):
    # A helper function to load the csv file.
    if not os.path.exists(path):
        raise Exception("The specified path {} does not exist.".format(path))
    # Initialize the data.
    team_ids = []
    features = []
    labels = []
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # skip header row

        for row in reader:
            try:
                team_id = int(row[0])
                # Next 2*num_champions columns: team + enemy picks
                team_picks = [int(x) for x in row[1:1+num_champions]]
                enemy_picks = [int(x) for x in row[1+num_champions:1+2*num_champions]]
                win = int(row[-1])

                team_ids.append(team_id)
                features.append(team_picks + enemy_picks)
                labels.append(win)

            except (ValueError, IndexError):
                # Skip malformed rows
                continue

    data = {
        "team_id": team_ids,
        "drafts": np.array(features, dtype=np.int32),
        "win": np.array(labels, dtype=np.int32)
    }
    return data


def load_train_sparse(root_dir="./data"):
    """Load the training data as a spare matrix representation.

    :param root_dir: str
    :return: 2D sparse matrix
    """
    # Load your CSV
    path_csv = os.path.join(root_dir, "train_data.csv")
    df = pd.read_csv(path_csv)

    # Drop team_id (just metadata, not needed for training matrix)
    feature_cols = df.columns.drop(["team_id", "win"])

    # Features: ally + enemy picks (one-hot)
    X = df[feature_cols].to_numpy(dtype=np.int8)

    # Labels: win
    y = df["win"].to_numpy(dtype=np.int8).reshape(-1, 1)

    # Convert to sparse
    sparse_X = csr_matrix(X)
    sparse_y = csr_matrix(y)

    # Combine features + label
    sparse_matrix = hstack([sparse_X, sparse_y], format="csr")

    # Save to disk
    save_path = os.path.join(root_dir, "train_sparse.npz")
    save_npz(save_path, sparse_matrix)

    path = os.path.join(root_dir, "train_sparse.npz")
    if not os.path.exists(path):
        raise Exception(
            "The specified path {} " "does not exist.".format(os.path.abspath(path))
        )
    matrix = load_npz(path)
    return matrix


def load_train_csv(root_dir="./data"):
    """Load the training data as a dictionary.

    :param root_dir: str
    :return: A dictionary {user_id: list, question_id: list, is_correct: list}
        WHERE
        user_id: a list of user id.
        question_id: a list of question id.
        is_correct: a list of binary value indicating the correctness of
        (user_id, question_id) pair.
    """
    path = os.path.join(root_dir, "train_data.csv")
    return _load_csv(path)


def load_valid_csv(root_dir="./data"):
    """Load the validation data as a dictionary.

    :param root_dir: str
    :return: A dictionary {user_id: list, question_id: list, is_correct: list}
        WHERE
        user_id: a list of user id.
        question_id: a list of question id.
        is_correct: a list of binary value indicating the correctness of
        (user_id, question_id) pair.
    """
    path = os.path.join(root_dir, "valid_data.csv")
    return _load_csv(path)


def load_public_test_csv(root_dir="./data"):
    """Load the test data as a dictionary.

    :param root_dir: str
    :return: A dictionary {user_id: list, question_id: list, is_correct: list}
        WHERE
        user_id: a list of user id.
        question_id: a list of question id.
        is_correct: a list of binary value indicating the correctness of
        (user_id, question_id) pair.
    """
    path = os.path.join(root_dir, "test_data.csv")
    return _load_csv(path)


def evaluate(data, predictions, threshold=0.5):
    """Return the accuracy of the predictions given the data.

    :param data: A dictionary {user_id: list, question_id: list, is_correct: list}
    :param predictions: list
    :param threshold: float
    :return: float
    """
    if len(data["win"]) != len(predictions):
        raise Exception("Mismatch of dimensions between data and prediction.")
    if isinstance(predictions, list):
        predictions = np.array(predictions).astype(np.float64)
    return np.sum((predictions >= threshold) == data["win"]) / float(
        len(data["win"])
    )


def sparse_matrix_evaluate(data, matrix, threshold=0.5):
    """Given the sparse matrix represent, return the accuracy of the prediction on data.

    :param data: A dictionary {user_id: list, question_id: list, is_correct: list}
    :param matrix: 2D matrix
    :param threshold: float
    :return: float
    """
    total_prediction = 0
    total_accurate = 0
    for i in range(len(data["win"])):
        cur_team_id = data["team_id"][i]
        cur_drafts = data["drafts"][i]
        if matrix[cur_team_id, cur_drafts] >= threshold and data["win"][i]:
            total_accurate += 1
        if matrix[cur_team_id, cur_drafts] < threshold and not data["win"][i]:
            total_accurate += 1
        total_prediction += 1
    return total_accurate / float(total_prediction)


def sparse_matrix_predictions(data, matrix, threshold=0.5):
    """Given the sparse matrix represent, return the predictions.

    This function can be used for submitting Kaggle competition.

    :param data: A dictionary {user_id: list, question_id: list, is_correct: list}
    :param matrix: 2D matrix
    :param threshold: float
    :return: list
    """
    predictions = []
    for i in range(len(data["team_id"])):
        cur_team_id = data["team_id"][i]
        cur_match_id = data["match_id"][i]
        if matrix[cur_team_id, cur_match_id] >= threshold:
            predictions.append(1.0)
        else:
            predictions.append(0.0)
    return predictions


def load_match_meta(path="./data/match_meta.csv"):
    """ Load the match metadata and return it as a dictionary.

    :return: A dictionary {match_id: list, team_b_id: list, team_r_id: list,
        team_b_picks: {int: list[int]}, team_r_picks: {int: list[int]}}
    """
    if not os.path.exists(path):
        raise Exception("The specified path {} does not exist.".format(path))
    # Initialize the data.
    data = {"match_id": [], "team_b_id": [], "team_r_id": [], "team_b_picks": {}, "team_r_picks": {}}
    # Iterate over the row to fill in the data.
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            try:
                data["match_id"].append(int(row[0]))
                data["team_b_id"].append(int(row[1]))
                data["team_r_id"].append(int(row[2]))
                data["team_b_picks"][int(row[0])] = list(row[3])
                data["team_r_picks"][int(row[0])] = list(row[4])
            except ValueError:
                # Pass first row.
                pass
            except IndexError:
                # is_correct might not be available.
                pass
    return data

