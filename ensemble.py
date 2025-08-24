from utils import (
    load_train_csv,
    load_valid_csv,
    load_public_test_csv,
    load_train_sparse,
)
import numpy as np
import matplotlib.pyplot as plt

from item_response import irt, sigmoid

# Manually set the seed for reproducibility
np.random.seed(67)

def generate_resample(data):
    """
    Generate and return a bootstrap sample of data

    :param data: A dictionary {user_id: list, question_id: list,
    is_correct: list}

    :return: A dictionary {user_id: list, question_id: list,
    is_correct: list}
    """
    N = len(data["user_id"])

    sample = {"user_id": [], "question_id": [], "is_correct": []}

    for _ in range(N):
        index = np.random.randint(N)
        sample["user_id"].append(data["user_id"][index])
        sample["question_id"].append(data["question_id"][index])
        sample["is_correct"].append(data["is_correct"][index])

    return sample


def evaluate(data, m_1, m_2, m_3):
    """
    Evaluate the ensemble of the models m_1, m_2, m_3 and
    return the accuracy.

    :param data: A dictionary {user_id: list, question_id: list,
    is_correct: list}

    :param m_1: (theta: Vector, beta: Vector)
    :param m_2: (theta: Vector, beta: Vector)
    :param m_3: (theta: Vector, beta: Vector)

    :return: float
    """
    pred = []
    for i, q in enumerate(data["question_id"]):
        u = data["user_id"][i]
        x_1 = (m_1[0][u] - m_1[1][q]).sum()
        x_2 = (m_2[0][u] - m_2[1][q]).sum()
        x_3 = (m_3[0][u] - m_3[1][q]).sum()

        pred.append(sigmoid(x_1) + sigmoid(x_2) + sigmoid(x_3) >= 1.5)

    return np.sum((data["is_correct"] == np.array(pred))) / len(data["is_correct"])


def main():
    train_data = load_train_csv("./data")
    val_data = load_valid_csv("./data")
    test_data = load_public_test_csv("./data")

    # Hyperparameters
    lr = 0.01
    iterations = 100

    print("Model 1")
    theta_1, beta_1, _, _, _ = irt(generate_resample(train_data), val_data, lr, iterations)
    print("Model 2")
    theta_2, beta_2, _, _, _ = irt(generate_resample(train_data), val_data, lr, iterations)
    print("Model 3")
    theta_3, beta_3, _, _, _ = irt(generate_resample(train_data), val_data, lr, iterations)

    val_acc = evaluate(val_data, (theta_1, beta_1), (theta_2, beta_2), (theta_3, beta_3))
    test_acc = evaluate(test_data, (theta_1, beta_1), (theta_2, beta_2), (theta_3, beta_3))

    print(f"Final validation accuracy: {val_acc}")
    print(f"Final test accuracy: {test_acc}")

if __name__ == "__main__":
    main()

