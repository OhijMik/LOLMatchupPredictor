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
    sparse_matrix = load_train_sparse("./data").toarray().astype(float)

    print("Sparse matrix:")
    print(sparse_matrix)
    print("Shape of sparse matrix:")
    print(sparse_matrix.shape)

    # Get all labeled entries
    team_ids, draft_ids = np.nonzero(~np.isnan(sparse_matrix))
    wins = sparse_matrix[team_ids, draft_ids]

    # Split for test set
    train_val_idx, test_idx = train_test_split(
        np.arange(len(draft_ids)),
        test_size=0.2,
        random_state=42
    )
    train_idx, val_idx = train_test_split(
        train_val_idx,
        test_size=0.25,  # 0.25 * 0.8 = 0.2 of total → 60/20/20 split
        random_state=42
    )

    # Build train and val dictionaries
    train_data = {
        "team_id": team_ids[train_idx],
        "draft_id": draft_ids[train_idx],
        "win": wins[train_idx]
    }
    val_data = {
        "team_id": team_ids[val_idx],
        "draft_id": draft_ids[val_idx],
        "win": wins[val_idx]
    }
    test_data = {
        "team_id": team_ids[test_idx],
        "draft_id": draft_ids[test_idx],
        "win": wins[test_idx]
    }

    # Mask validation entries in the sparse matrix for val data
    sparse_matrix_masked_val = sparse_matrix.copy()
    sparse_matrix_masked_val[val_data["team_id"], val_data["draft_id"]] = np.nan

    k_values = [1, 3, 10]
    val_accuracies = []

    for k in k_values:
        print(f"k={k}")
        acc = knn_impute_by_team(sparse_matrix_masked_val, val_data, k)
        val_accuracies.append(acc)

    # Find the best k for user-based
    best_k = k_values[np.argmax(val_accuracies)]
    print(f"\nBest k (team-based): {best_k}")

    # Mask validation entries in the sparse matrix for test data
    sparse_matrix_masked_test = sparse_matrix.copy()
    sparse_matrix_masked_test[test_data["team_id"], test_data["draft_id"]] = np.nan

    # Evaluate on test data with best k
    print("Test accuracy of best k (user-based): ")
    nbrs = KNNImputer(n_neighbors=best_k)
    # We use NaN-Euclidean distance measure.
    mat = nbrs.fit_transform(sparse_matrix_masked_test)
    acc = sparse_matrix_evaluate(test_data, mat)
    print("Test Accuracy: {}".format(acc))
    print("")

    # Mask any entries you want to predict as NaN (if not already missing)
    team_idx = 8  # the integer index for the team
    draft_idx = 301  # the integer index for the draft
    sparse_matrix[draft_idx, team_idx] = np.nan

    # Apply KNN imputer with your chosen best k
    imputer = KNNImputer(n_neighbors=best_k)
    imputed_matrix = imputer.fit_transform(sparse_matrix)

    # Get the predicted win probability
    predicted_win_prob = imputed_matrix[draft_idx, team_idx]

    # Convert to binary prediction
    predicted_win = int(predicted_win_prob >= 0.5)
    print(f"Predicted probability: {predicted_win_prob:.3f}, Predicted win: {predicted_win}")


if __name__ == "__main__":
    main()
