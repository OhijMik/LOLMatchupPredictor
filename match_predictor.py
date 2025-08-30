import numpy as np
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

from utils import (
    draft_to_vector, load_train_csv, load_valid_csv,
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
    X, y, team_ids = load_train_csv("./data")

    # Split train/val/test
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    k_values = [1, 3, 10]
    val_accuracies = []

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        val_acc = knn.score(X_val, y_val)
        val_accuracies.append(val_acc)
        print(f"k={k}, Validation Accuracy={val_acc:.4f}")

    best_k = k_values[np.argmax(val_accuracies)]
    print(f"\nBest k: {best_k}")

    # Retrain on train+val
    knn = KNeighborsClassifier(n_neighbors=best_k)
    knn.fit(np.vstack([X_train, X_val]), np.hstack([y_train, y_val]))
    test_acc = knn.score(X_test, y_test)
    print(f"Test Accuracy: {test_acc:.4f}")

    # Example prediction
    ally_draft = [1, 34, 67, 102, 140]  # champion IDs
    enemy_draft = [3, 50, 72, 101, 160]
    x_new = np.array([draft_to_vector(ally_draft, enemy_draft)])
    pred_prob = knn.predict_proba(x_new)[0][1]
    pred_win = int(pred_prob >= 0.5)

    print(f"Predicted win probability: {pred_prob:.3f}, Predicted win: {pred_win}")


if __name__ == "__main__":
    main()
