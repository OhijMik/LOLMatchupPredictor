import csv
import pandas as pd

# Team name to ID mapping
team_meta = pd.read_csv("data/team_meta.csv")
team_to_id = dict(zip(team_meta["name"], team_meta["team_id"]))

# Champion name to ID mapping
champion_name_meta = pd.read_csv("data/champion_meta.csv")
champ_to_id = dict(zip(champion_name_meta["name"], champion_name_meta["champion_id"]))

# Input data with winner column
input_data = """Hanwha Life Esports	Karmine Corp	Hanwha Life Esports	Camille,Vi,Ahri,Xayah,Gragas	Kennen,Pantheon,Galio,Draven,Renata Glasc
Karmine Corp	Hanwha Life Esports	Hanwha Life Esports	Gangplank,Sejuani,Viktor,Jhin,Rell	Jax,Xin Zhao,Sylas,Ashe,Sett
Hanwha Life Esports	Karmine Corp	Hanwha Life Esports	Gnar,Skarner,Aurora,Varus,Braum	Aatrox,Ivern,Hwei,Ezreal,Leona
Hanwha Life Esports	Karmine Corp	Karmine Corp	Rumble,Wukong,Azir,Kai'Sa,Alistar	Jayce,Maokai,Taliyah,Miss Fortune,Rakan
Top Esports	Hanwha Life Esports	Hanwha Life Esports	Ambessa,Pantheon,Aurora,Corki,Bard	Jax,Maokai,Vladimir,Jhin,Blitzcrank
Top Esports	Hanwha Life Esports	Hanwha Life Esports	Renekton,Xin Zhao,Sylas,Varus,Nautilus	Aatrox,Vi,Akali,Ashe,Rell
Hanwha Life Esports	Top Esports	Hanwha Life Esports	Rumble,Wukong,Azir,Ezreal,Alistar	Jayce,Sejuani,Yone,Miss Fortune,Rakan
Karmine Corp	CTBC Flying Oyster	Karmine Corp	Jax,Maokai,Corki,Nilah,Senna	Gangplank,Skarner,Orianna,Zeri,Yuumi
CTBC Flying Oyster	Karmine Corp	CTBC Flying Oyster	Ornn,Nocturne,Akali,Kalista,Renata Glasc	Gnar,Wukong,Aurora,Caitlyn,Karma
Karmine Corp	CTBC Flying Oyster	CTBC Flying Oyster	Ambessa,Vi,Hwei,Jhin,Pyke	Renekton,Nidalee,Tristana,Ashe,Thresh
CTBC Flying Oyster	Karmine Corp	Karmine Corp	Gragas,Kindred,Galio,Ezreal,Nautilus	Aatrox,Pantheon,Taliyah,Kai'Sa,Rell
CTBC Flying Oyster	Karmine Corp	Karmine Corp	Rumble,Xin Zhao,Azir,Sivir,Alistar	Jayce,Sejuani,Yone,Varus,Leona
Hanwha Life Esports	Team Liquid	Hanwha Life Esports	Ambessa,Skarner,Kassadin,Sivir,Braum	Jax,Ivern,Viktor,Ezreal,Leona
Team Liquid	Hanwha Life Esports	Team Liquid	Renekton,Maokai,Cassiopeia,Varus,Rakan	Quinn,Zyra,Tristana,Jhin,Rell
Team Liquid	Hanwha Life Esports	Hanwha Life Esports	K'Sante,Pantheon,Ziggs,Kalista,Renata Glasc	Kayle,Vi,Ryze,Draven,Pyke
Top Esports	CTBC Flying Oyster	CTBC Flying Oyster	Rumble,Xin Zhao,Sylas,Corki,Poppy	Sion,Skarner,Azir,Caitlyn,Nautilus
CTBC Flying Oyster	Top Esports	CTBC Flying Oyster	Jayce,Sejuani,Taliyah,Ezreal,Alistar	K'Sante,Nidalee,Yone,Jhin,Leona
Hanwha Life Esports	Karmine Corp	Hanwha Life Esports	Vladimir,Wukong,Jayce,Kai'Sa,Rell	Sion,Sejuani,Ryze,Draven,Rakan
Karmine Corp	Hanwha Life Esports	Karmine Corp	Ambessa,Ivern,Azir,Jhin,Alistar	Gnar,Maokai,Corki,Ashe,Renata Glasc
Karmine Corp	Hanwha Life Esports	Hanwha Life Esports	Rumble,Xin Zhao,Taliyah,Ezreal,Leona	Aurora,Vi,Sylas,Varus,Poppy
Team Liquid	CTBC Flying Oyster	CTBC Flying Oyster	Jax,Sejuani,Corki,Ziggs,Poppy	Gangplank,Maokai,Yone,Tristana,Leona
Team Liquid	CTBC Flying Oyster	CTBC Flying Oyster	Gwen,Vi,Taliyah,Kai'Sa,Rakan	K'Sante,Xin Zhao,Azir,Ezreal,Alistar
Top Esports	Karmine Corp	Karmine Corp	Gnar,Karthus,Corki,Varus,Rell	Aatrox,Ivern,Yone,Ezreal,Leona
Top Esports	Karmine Corp	Karmine Corp	Ambessa,Viego,Aurora,Kalista,Renata Glasc	Jayce,Skarner,Taliyah,Ashe,Karma
CTBC Flying Oyster	Hanwha Life Esports	Hanwha Life Esports	Gragas,Kindred,Taliyah,Corki,Leona	Vladimir,Nidalee,Zed,Miss Fortune,Rell
Hanwha Life Esports	CTBC Flying Oyster	Hanwha Life Esports	Rumble,Vi,Yone,Ashe,Rakan	Karma,Wukong,Azir,Ezreal,Alistar
Team Liquid	Top Esports	Top Esports	K'Sante,Maokai,Hwei,Kalista,Nautilus	Aatrox,Pantheon,Sylas,Varus,Neeko
Top Esports	Team Liquid	Top Esports	Rumble,Vi,Aurora,Ashe,Braum	Galio,Xin Zhao,Tristana,Ezreal,Rakan
Karmine Corp	CTBC Flying Oyster	CTBC Flying Oyster	Jayce,Brand,Yone,Varus,Nautilus	Sion,Sejuani,Taliyah,Miss Fortune,Rell
CTBC Flying Oyster	Karmine Corp	CTBC Flying Oyster	Rumble,Skarner,Viktor,Ezreal,Leona	Ambessa,Vi,Aurora,Kai'Sa,Rakan
Top Esports	Hanwha Life Esports	Hanwha Life Esports	Gragas,Nocturne,Orianna,Kalista,Renata Glasc	Aatrox,Nidalee,Akali,Varus,Poppy
Hanwha Life Esports	Top Esports	Hanwha Life Esports	Jax,Skarner,Azir,Ezreal,Alistar	Kennen,Vi,Aurora,Miss Fortune,Leona
Team Liquid	Karmine Corp	Team Liquid	K'Sante,Nocturne,Taliyah,Lucian,Nami	Gnar,Xin Zhao,Ahri,Zeri,Yuumi
Karmine Corp	Team Liquid	Karmine Corp	Camille,Sejuani,Azir,Miss Fortune,Leona	Ambessa,Skarner,Aurelion Sol,Ashe,Pantheon
Karmine Corp	Team Liquid	Team Liquid	Jayce,Vi,Aurora,Ezreal,Rell	Ornn,Maokai,Tristana,Varus,Nautilus"""

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
