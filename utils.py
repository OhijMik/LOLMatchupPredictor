import numpy as np
import os
import pandas as pd
import ast


# Load champion meta
champion_name_meta = pd.read_csv("data/champion_meta.csv")
# Create name -> id mapping
name_to_id = dict(zip(champion_name_meta["name"], champion_name_meta["champion_id"]))

champion_meta = pd.read_csv("data/champion_meta.csv", index_col="champion_id")
# Drop "name" because it's not numeric
champion_features = champion_meta.drop(columns=["name"]).to_numpy()

num_champions = champion_features.shape[0]
num_roles = champion_features.shape[1]


def draft_to_vector(ally_picks, enemy_picks):
    """Convert ally + enemy champions into a binary feature vector."""
    vec = np.zeros(2 * num_champions, dtype=np.int32)
    for champ in ally_picks:
        vec[champ - 1] = 1
    for champ in enemy_picks:
        vec[num_champions + champ - 1] = 1

    # Role/class feature part
    ally_roles = np.sum(champion_features[np.array(ally_picks) - 1], axis=0)
    enemy_roles = np.sum(champion_features[np.array(enemy_picks) - 1], axis=0)

    # Concatenate: [binary_draft, ally_roles, enemy_roles]
    return np.concatenate([ally_roles, enemy_roles])


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
    df = pd.read_csv(path)

    # Parse champion picks
    df["ally_draft"] = df["ally_draft"].apply(ast.literal_eval)
    df["enemy_draft"] = df["enemy_draft"].apply(ast.literal_eval)

    # Convert drafts to binary vectors
    X = np.array([draft_to_vector(ally, enemy) for ally, enemy in zip(df["ally_draft"], df["enemy_draft"])])
    y = df["win"].to_numpy()
    team_ids = df["team_id"].to_numpy()

    return X, y, team_ids


def names_to_ids(draft_names):
    """Convert a list of champion names to a list of champion IDs."""
    return [name_to_id[name] for name in draft_names]
