import numpy as np
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from utils import (
    load_valid_csv,
    load_public_test_csv,
    load_train_sparse,
    sparse_matrix_evaluate,
)


def knn_impute_by_team(matrix, valid_data, k):
    """Fill in the missing values using k-Nearest Neighbors based on
    team similarity. Return the accuracy on valid_data.

    See https://scikit-learn.org/stable/modules/generated/sklearn.
    impute.KNNImputer.html for details.

    :param matrix: 2D sparse matrix
    :param valid_data: A dictionary {user_id: list, question_id: list,
    is_correct: list}
    :param k: int
    :return: float
    """
    nbrs = KNNImputer(n_neighbors=k)
    # We use NaN-Euclidean distance measure.
    mat = nbrs.fit_transform(matrix)
    acc = sparse_matrix_evaluate(valid_data, mat)
    print("Validation Accuracy: {}".format(acc))
    return acc


def main():
    sparse_matrix = load_train_sparse("./data")
    test_data = load_public_test_csv("./data")

    # Convert IDs to 0-based (Python indexing)
    test_data["match_id"] = np.array(test_data["match_id"]) - 1
    test_data["team_id"] = np.array(test_data["team_id"]) - 1

    # Determine dimensions to include all match IDs (train + test)
    num_teams = sparse_matrix.shape[0]
    max_match_id = max(sparse_matrix.shape[1], max(test_data["match_id"]) + 1)

    # Expand the matrix to cover all match IDs
    expanded_matrix = np.full((num_teams, max_match_id), np.nan)
    expanded_matrix[:, :sparse_matrix.shape[1]] = sparse_matrix

    # Get all labeled entries for train/val split
    team_ids, match_ids = np.nonzero(~np.isnan(expanded_matrix))
    wins = expanded_matrix[team_ids, match_ids]

    # Split indices into train and validation
    train_idx, val_idx = train_test_split(
        np.arange(len(match_ids)), test_size=0.2, random_state=42
    )

    # Build train and val dictionaries
    train_data = {
        "team_id": team_ids[train_idx],
        "match_id": match_ids[train_idx],
        "win": wins[train_idx]
    }
    val_data = {
        "team_id": team_ids[val_idx],
        "match_id": match_ids[val_idx],
        "win": wins[val_idx]
    }

    # Mask validation entries in matrix for proper KNN training
    masked_matrix = expanded_matrix.copy()
    masked_matrix[val_data["team_id"], val_data["match_id"]] = np.nan

    k_values = [1, 3, 10]
    val_accuracies = []

    for k in k_values:
        acc = knn_impute_by_team(masked_matrix, val_data, k)
        val_accuracies.append(acc)
        print(f"k={k}, Validation Accuracy={acc:.4f}")

    # Find the best k for user-based
    best_k = k_values[np.argmax(val_accuracies)]
    print(f"\nBest k (user-based): {best_k}")

    # Evaluate on test data with best k
    print("Test accuracy of best k (user-based): ")
    print(masked_matrix.shape)
    knn_impute_by_team(masked_matrix, test_data, best_k)
    print("")


if __name__ == "__main__":
    main()
