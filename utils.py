import numpy as np
import os
import pandas as pd
import ast


# Load champion meta
champion_name_meta = pd.read_csv("data/champion_meta(mobalytics)2.csv")
# Create name -> id mapping
name_to_id = dict(zip(champion_name_meta["name"], champion_name_meta["champion_id"]))

champion_meta = pd.read_csv("data/champion_meta(mobalytics)2.csv", index_col="champion_id")
# Drop "name"
champion_features = champion_meta.drop(columns=["name"]).to_numpy()

num_champions = champion_features.shape[0]
num_roles = champion_features.shape[1]


def draft_to_vector(ally_picks, enemy_picks):
    """Convert ally + enemy champions into a binary feature vector."""
    # Role/class feature part
    ally_roles = np.sum(champion_features[np.array(ally_picks) - 1], axis=0)
    enemy_roles = np.sum(champion_features[np.array(enemy_picks) - 1], axis=0)
    # ally_roles = champion_features[np.array(ally_picks) - 1].flatten()
    # enemy_roles = champion_features[np.array(enemy_picks) - 1].flatten()

    # Concatenate: [ally_roles, enemy_roles]
    return np.concatenate([ally_roles, enemy_roles])


def load_train_csv(root_dir="./data"):
    """Load training data with ally/enemy drafts."""
    path = os.path.join(root_dir, "train_data.csv")
    df = pd.read_csv(path)

    # Parse champion picks
    df["ally_draft"] = df["ally_draft"].apply(ast.literal_eval)
    df["enemy_draft"] = df["enemy_draft"].apply(ast.literal_eval)

    # Convert drafts to vectors
    draft_X = np.array([draft_to_vector(ally, enemy) for ally, enemy in zip(df["ally_draft"], df["enemy_draft"])])

    # One-hot encode team_id
    unique_team_ids = sorted(df["team_id"].unique())
    team_id_to_index = {tid: i for i, tid in enumerate(unique_team_ids)}

    team_one_hot = np.zeros((len(df), len(unique_team_ids)), dtype=np.int32)
    for i, tid in enumerate(df["team_id"]):
        team_one_hot[i, team_id_to_index[tid]] = 1

    # Final feature matrix: [draft_features, team_id_onehot]
    X = np.hstack([draft_X, team_one_hot])

    y = df["win"].to_numpy()

    return X, y


def names_to_ids(draft_names):
    """Convert a list of champion names to a list of champion IDs."""
    return [name_to_id[name] for name in draft_names]
