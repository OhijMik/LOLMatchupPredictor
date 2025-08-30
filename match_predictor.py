import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import ast

from utils import (
    draft_to_vector,
    load_train_csv,
    names_to_ids
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

    # # Example prediction 1
    # ally_draft = [1, 34, 67, 102, 140]  # champion IDs
    # enemy_draft = [3, 50, 72, 101, 160]
    # pred_class, pred_prob = predict_draft(knn, ally_draft, enemy_draft)
    #
    # print(f"Predicted win: {pred_class}, Probability: {pred_prob:.2f}\n")
    #
    # # Example prediction 2
    # ally_draft = ["Ambessa", "Wukong", "Azir", "Corki", "Bard"]  # champion names
    # enemy_draft = ["Rumble", "Sejuani", "Yone", "Varus", "Karma"]
    #
    # # Convert names to IDs
    # ally_ids = names_to_ids(ally_draft)
    # enemy_ids = names_to_ids(enemy_draft)
    #
    # pred_class, pred_prob = predict_draft(knn, ally_ids, enemy_ids)
    #
    # print(f"Predicted win: {pred_class}, Probability: {pred_prob:.2f}\n")

    # Example prediction 3
    predict_file = pd.read_csv("data/predict.csv").reset_index(drop=True)

    for i in range(len(predict_file["team_id"])):
        ally_names = ast.literal_eval(predict_file.loc[i, "ally_draft"])
        enemy_names = ast.literal_eval(predict_file.loc[i, "enemy_draft"])

        ally_ids = names_to_ids(ally_names)
        enemy_ids = names_to_ids(enemy_names)

        pred_class, pred_prob = predict_draft(knn, ally_ids, enemy_ids)

        print(f"Match {i + 1}, Predicted win: {pred_class}, Probability: {pred_prob:.2f}\n")


if __name__ == "__main__":
    main()
