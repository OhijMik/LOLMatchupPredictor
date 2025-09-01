import csv
import pandas as pd

# Team name to ID mapping
team_meta = pd.read_csv("data/team_meta.csv")
team_to_id = dict(zip(team_meta["name"], team_meta["team_id"]))

# Champion name to ID mapping
champion_name_meta = pd.read_csv("data/champion_meta.csv")
champ_to_id = dict(zip(champion_name_meta["name"], champion_name_meta["champion_id"]))

# Input data with winner column
input_data = """FlyQuest	Shopify Rebellion	FlyQuest	Sion,Tryndamere,Syndra,Xayah,Rakan	Gnar,Skarner,Hwei,Corki,Leona
FlyQuest	Shopify Rebellion	FlyQuest	Ambessa,Trundle,Ryze,Kai'Sa,Rell	Aatrox,Vi,Galio,Ezreal,Braum
FlyQuest	Shopify Rebellion	Shopify Rebellion	Rumble,Poppy,Taliyah,Senna,Alistar	Aurora,Xin Zhao,Annie,Lucian,Nami
FlyQuest	Shopify Rebellion	FlyQuest	Renekton,Sejuani,Viktor,Yunara,Bard	K'Sante,Wukong,Orianna,Varus,Nautilus
Team Liquid	100 Thieves	100 Thieves	Gangplank,Poppy,Taliyah,Varus,Nautilus	Renekton,Sejuani,Ryze,Sivir,Renata Glasc
Team Liquid	100 Thieves	100 Thieves	Sion,Viego,Annie,Yunara,Blitzcrank	K'Sante,Trundle,Aurora,Corki,Rakan
Team Liquid	100 Thieves	100 Thieves	Galio,Wukong,Ziggs,Lucian,Alistar	Rumble,Xin Zhao,Orianna,Jhin,Neeko
Cloud9	Disguised	Cloud9	Rek'Sai,Zyra,Zeri,Senna,Leona	Gnar,Jarvan IV,Cassiopeia,Miss Fortune,Rakan
Cloud9	Disguised	Disguised	Yorick,Xin Zhao,Hwei,Jhin,Alistar	Jax,Sylas,Viktor,Lucian,Braum
Cloud9	Disguised	Disguised	Aatrox,Skarner,Ryze,Smolder,Blitzcrank	Sion,Poppy,Anivia,Ezreal,Rell
Disguised	Cloud9	Cloud9	Gwen,Vi,Galio,Kai'Sa,Nautilus	Renekton,Trundle,Orianna,Xayah,Neeko
Cloud9	Disguised	Cloud9	Ambessa,Wukong,Azir,Corki,Bard	Rumble,Sejuani,Yone,Varus,Karma"""

# Process the data
blue_team_data = []
red_team_data = []

for line in input_data.split('\n'):
    parts = line.split('\t')
    if len(parts) >= 5:  # Skip header and empty lines
        blue_team = parts[0].strip()
        red_team = parts[1].strip()
        winner = parts[2].strip()
        blue_draft = parts[3].split(',')
        red_draft = parts[4].split(',')

        # Convert champion names to IDs
        blue_draft_ids = [str(champ_to_id[champ.strip()]) for champ in blue_draft]
        red_draft_ids = [str(champ_to_id[champ.strip()]) for champ in red_draft]

        # Determine win/loss (1 for win, 0 for loss)
        blue_win = 1 if winner == blue_team else 0
        red_win = 1 if winner == red_team else 0

        # Blue team perspective
        blue_team_data.append([
            team_to_id[blue_team],
            f"[{', '.join(blue_draft_ids)}]",
            f"[{', '.join(red_draft_ids)}]",
            blue_win
        ])

        # Red team perspective
        red_team_data.append([
            team_to_id[red_team],
            f"[{', '.join(red_draft_ids)}]",
            f"[{', '.join(blue_draft_ids)}]",
            red_win
        ])

# Append to existing CSV files (create if they don't exist)
with open('data/temp_train_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(blue_team_data)

with open('data/temp_train_data.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(red_team_data)
