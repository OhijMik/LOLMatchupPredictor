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

def predict_draft(knn_model, ally_draft, enemy_draft):
    """
    Predict win probability or class for a given draft.

    :param knn_model: trained KNeighborsClassifier
    :param ally_picks: list of ally champion_ids (1-indexed)
    :param enemy_picks: list of enemy champion_ids (1-indexed)
    :return: predicted class (0/1) and probability of winning
    """
    # Convert draft to vector with role/class features
    draft_vec = draft_to_vector(ally_draft, enemy_draft).reshape(1, -1)

    # Predict probability and class
    win_prob = knn_model.predict_proba(draft_vec)[0][1]  # probability of winning
    win_class = knn_model.predict(draft_vec)[0]          # predicted class 0/1

    return win_class, win_prob


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
    pred_class, pred_prob = predict_draft(knn, ally_draft, enemy_draft)

    print(f"Predicted win: {pred_class}, Probability: {pred_prob:.2f}")


if __name__ == "__main__":
    main()
