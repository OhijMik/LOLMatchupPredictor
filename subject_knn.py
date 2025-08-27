import numpy as np
from SubjectWeightedKNNImputer import SubjectWeightedKNNImputer
import matplotlib.pyplot as plt
from utils import (
    load_valid_csv,
    load_public_test_csv,
    load_train_sparse,
    sparse_matrix_evaluate,
    load_question_meta
)
from knn import knn_impute_by_match


def sw_knn_impute_by_user(matrix, valid_data, k, overlap):
    """Fill in the missing values using k-Nearest Neighbors based on
    student similarity. Return the accuracy on valid_data.

    See https://scikit-learn.org/stable/modules/generated/sklearn.
    impute.KNNImputer.html for details.

    :param matrix: 2D sparse matrix
    :param valid_data: A dictionary {user_id: list, question_id: list,
    is_correct: list}
    :param k: int
    :param overlap: int
    :return: float
    """
    nbrs = SubjectWeightedKNNImputer(n_neighbors=k, min_overlap=overlap)

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

    #####################################################################
    # TODO:                                                             #
    # Compute the validation accuracy for each k. Then pick k* with     #
    # the best performance and report the test accuracy with the        #
    # chosen k*.                                                        #
    #####################################################################
    k_values = [1, 3, 5, 7, 9, 11, 15, 21, 26]

    # Compute user based KNN
    user_val_accuracies = []
    print("User based")
    for k in k_values:
        print(f"Testing k: {k}")
        accuracy = knn_impute_by_user(sparse_matrix, val_data, k)
        user_val_accuracies.append(accuracy)

    # Compute question based KNN
    item_val_accuracies = []
    print("Item based")
    for k in k_values:
        print(f"Testing k: {k}")
        accuracy = knn_impute_by_item(sparse_matrix, val_data, k)
        item_val_accuracies.append(accuracy)

    # Compute subject/user based KNN
    user_sw_val_accuracies = []
    print("User based and subject weighted")
    for k in k_values:
        print(f"Testing k: {k}")
        accuracy = sw_knn_impute_by_user(sparse_matrix, val_data, k, 1)
        user_sw_val_accuracies.append(accuracy)

    # Plot user-based
    plt.figure(figsize=(8, 5))
    plt.plot(k_values, user_val_accuracies, label="User Based", marker='o')
    plt.plot(k_values, item_val_accuracies, label="Item Based", marker='o')
    plt.plot(k_values, user_sw_val_accuracies, label="Subject Weighted", marker='o')
    plt.title("Validation Accuracy vs. k -- User based, Item based, Subject Weighted")
    plt.xlabel("k")
    plt.ylabel("Validation Accuracy")
    plt.grid(True)
    plt.show()

    # Find the best k for user-based
    best_k = k_values[np.argmax(user_val_accuracies)]
    print(f"\nBest k (user-based): {best_k}")
    # Evaluate on test data with best k
    print("Test accuracy of best k (user-based): ")
    sw_knn_impute_by_user(sparse_matrix, test_data, best_k, 1)
    print("")


    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################


if __name__ == "__main__":
    main()
