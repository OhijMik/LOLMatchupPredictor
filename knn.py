import numpy as np
from sklearn.impute import KNNImputer
import matplotlib.pyplot as plt
from utils import (
    load_valid_csv,
    load_public_test_csv,
    load_train_sparse,
    sparse_matrix_evaluate,
)


def knn_impute_by_team(matrix, valid_data, k):
    """Fill in the missing values using k-Nearest Neighbors based on
    team picks similarity. Return the accuracy on valid_data.

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
    sparse_matrix = load_train_sparse("./data").toarray()
    val_data = load_valid_csv("./data")
    test_data = load_public_test_csv("./data")

    print("Sparse matrix:")
    print(sparse_matrix)
    print("Shape of sparse matrix:")
    print(sparse_matrix.shape)

    k_values = [1, 3, 10]

    # Compute user-based KNN
    user_val_accuracies = []
    for k in k_values:
        accuracy = knn_impute_by_team(sparse_matrix, val_data, k)
        user_val_accuracies.append(accuracy)

    # Plot user-based
    plt.figure(figsize=(8, 5))
    plt.plot(k_values, user_val_accuracies, marker='o')
    plt.title("Validation Accuracy vs. k -- User based")
    plt.xlabel("k")
    plt.ylabel("Validation Accuracy")
    plt.grid(True)
    plt.show()

    # Find the best k for user-based
    best_k = k_values[np.argmax(user_val_accuracies)]
    print(f"\nBest k (user-based): {best_k}")
    # Evaluate on test data with best k
    print("Test accuracy of best k (user-based): ")
    knn_impute_by_team(sparse_matrix, test_data, best_k)
    print("")


if __name__ == "__main__":
    main()
