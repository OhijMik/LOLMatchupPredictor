import csv
import pandas as pd

# Team name to ID mapping
team_meta = pd.read_csv("data/team_meta.csv")
team_to_id = dict(zip(team_meta["name"], team_meta["team_id"]))

# Champion name to ID mapping
champion_name_meta = pd.read_csv("data/champion_meta.csv")
champ_to_id = dict(zip(champion_name_meta["name"], champion_name_meta["champion_id"]))

# Input data with winner column
input_data = """Ultra Prime	Weibo Gaming	Weibo Gaming	Renekton,Vi,Aurora,Kai'Sa,Maokai	K'Sante,Zed,Ryze,Yunara,Rakan
Ultra Prime	Weibo Gaming	Weibo Gaming	Ambessa,Xin Zhao,Galio,Varus,Bard	Gwen,Naafiri,Annie,Sivir,Alistar
Weibo Gaming	Ultra Prime	Weibo Gaming	Rumble,Trundle,Taliyah,Jhin,Rell	Sion,Jarvan IV,Orianna,Corki,Neeko
EDward Gaming	Team WE	EDward Gaming	Aatrox,Poppy,Orianna,Senna,Braum	Renekton,Olaf,Galio,Jhin,Karma
Team WE	EDward Gaming	Team WE	Sion,Wukong,Corki,Ziggs,Alistar	Ambessa,Pantheon,Akali,Ezreal,Bard
Team WE	EDward Gaming	EDward Gaming	Yorick,Trundle,Taliyah,Varus,Leona	Jax,Jarvan IV,Ahri,Sivir,Nautilus
Team WE	EDward Gaming	EDward Gaming	Rumble,Vi,Aurora,Yunara,Rell	Ornn,Xin Zhao,Ryze,Kai'Sa,Neeko
FunPlus Phoenix	Ninjas in Pyjamas.CN	Ninjas in Pyjamas.CN	Jax,Poppy,Annie,Xayah,Taric	Udyr,Nidalee,Sylas,Jinx,Leona
Ninjas in Pyjamas.CN	FunPlus Phoenix	Ninjas in Pyjamas.CN	Aatrox,Jarvan IV,Akali,Smolder,Neeko	K'Sante,Zed,Ahri,Kai'Sa,Bard
FunPlus Phoenix	Ninjas in Pyjamas.CN	FunPlus Phoenix	Aurora,Sejuani,Yone,Lucian,Braum	Sion,Viego,Viktor,Jhin,Renata Glasc
Ninjas in Pyjamas.CN	FunPlus Phoenix	Ninjas in Pyjamas.CN	Ambessa,Wukong,Orianna,Zeri,Alistar	Renekton,Skarner,Taliyah,Corki,Nautilus
FunPlus Phoenix	Ninjas in Pyjamas.CN	FunPlus Phoenix	Gwen,Xin Zhao,Galio,Varus,Rakan	Rumble,Vi,Ryze,Sivir,Rell"""

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
