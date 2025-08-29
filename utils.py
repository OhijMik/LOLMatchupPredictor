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
    data = {"team_id": [], "draft_id": [], "win": []}
    # Iterate over the row to fill in the data.
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            try:
                data["draft_id"].append(int(row[0]))
                data["team_id"].append(int(row[1]))
                data["win"].append(int(row[2]))
            except ValueError:
                # Pass first row.
                pass
            except IndexError:
                # is_correct might not be available.
                pass
    return data


def load_train_sparse(root_dir="./data"):
    """Load the training data as a spare matrix representation.

    :param root_dir: str
    :return: 2D sparse matrix
    """
    # Load your CSV into a pandas DataFrame
    df = pd.read_csv(os.path.join(root_dir, "train_data.csv"))

    rows = df["draft_id"].to_numpy()
    cols = df["team_id"].to_numpy()
    vals = df["win"].to_numpy()

    sparse_matrix = csr_matrix((vals, (rows, cols)))

    # Save as an .npz file
    path = os.path.join(root_dir, "train_sparse.npz")
    save_npz(path, sparse_matrix)

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
        cur_draft_id = data["draft_id"][i]
        if matrix[cur_team_id, cur_draft_id] >= threshold and data["win"][i]:
            total_accurate += 1
        if matrix[cur_team_id, cur_draft_id] < threshold and not data["win"][i]:
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
        cur_match_id = data["draft_id"][i]
        if matrix[cur_team_id, cur_match_id] >= threshold:
            predictions.append(1.0)
        else:
            predictions.append(0.0)
    return predictions

