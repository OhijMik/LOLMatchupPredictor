import csv
import pandas as pd

# Team name to ID mapping
team_meta = pd.read_csv("data/team_meta.csv")
team_to_id = dict(zip(team_meta["name"], team_meta["team_id"]))

# Champion name to ID mapping
champion_name_meta = pd.read_csv("data/champion_meta.csv")
champ_to_id = dict(zip(champion_name_meta["name"], champion_name_meta["champion_id"]))

# Input data with winner column
input_data = """GAM Esports	Team Secret Whales	GAM Esports	Renekton,Viego,Taliyah,Sivir,Alistar	K'Sante,Vi,Ahri,Varus,Rakan
GAM Esports	Team Secret Whales	GAM Esports	Sion,Pantheon,Galio,Corki,Rell	Aatrox,Wukong,Annie,Ezreal,Neeko
Fukuoka SoftBank HAWKS gaming	DetonatioN FocusMe	DetonatioN FocusMe	Gwen,Pantheon,Ryze,Jhin,Rell	Jax,Trundle,Taliyah,Lucian,Braum
DetonatioN FocusMe	Fukuoka SoftBank HAWKS gaming	DetonatioN FocusMe	Rumble,Nocturne,Orianna,Smolder,Nautilus	K'Sante,Xin Zhao,Annie,Corki,Rakan
Team Secret Whales	MGN Vikings Esports	Team Secret Whales	Jayce,Poppy,Orianna,Xayah,Rakan	K'Sante,Xin Zhao,Hwei,Miss Fortune,Rell
MGN Vikings Esports	Team Secret Whales	MGN Vikings Esports	Udyr,Jarvan IV,Ziggs,Yunara,Alistar	Sion,Pantheon,Azir,Corki,Bard
Team Secret Whales	MGN Vikings Esports	Team Secret Whales	Ambessa,Wukong,Annie,Sivir,Neeko	Yorick,Vi,Ryze,Varus,Nautilus
Fukuoka SoftBank HAWKS gaming	Chiefs Esports Club	Fukuoka SoftBank HAWKS gaming	Ambessa,Skarner,Orianna,Sivir,Neeko	Yorick,Kindred,Galio,Kai'Sa,Nautilus
Chiefs Esports Club	Fukuoka SoftBank HAWKS gaming	Chiefs Esports Club	Rumble,Nocturne,Aurora,Smolder,Alistar	Ornn,Trundle,Ryze,Lucian,Braum
Fukuoka SoftBank HAWKS gaming	Chiefs Esports Club	Fukuoka SoftBank HAWKS gaming	K'Sante,Xin Zhao,Annie,Yunara,Rakan	Rek'Sai,Qiyana,Azir,Corki,Rell
GAM Esports	CTBC Flying Oyster	CTBC Flying Oyster	Renekton,Viego,Annie,Kog'Maw,Braum	Sion,Trundle,Orianna,Sivir,Rakan
CTBC Flying Oyster	GAM Esports	CTBC Flying Oyster	Rumble,Wukong,Azir,Kai'Sa,Neeko	Galio,Xin Zhao,Aurora,Corki,Bard
PSG Talon	DetonatioN FocusMe	PSG Talon	Ambessa,Pantheon,Viktor,Lucian,Braum	K'Sante,Qiyana,Aurora,Corki,Bard
PSG Talon	DetonatioN FocusMe	PSG Talon	Galio,Vi,Taliyah,Varus,Nautilus	Rumble,Trundle,Ryze,Jhin,Neeko
Fukuoka SoftBank HAWKS gaming	DetonatioN FocusMe	DetonatioN FocusMe	Mordekaiser,Vi,Viktor,Lucian,Rell	Sion,Talon,Aurora,Senna,Blitzcrank
DetonatioN FocusMe	Fukuoka SoftBank HAWKS gaming	DetonatioN FocusMe	K'Sante,Zed,Taliyah,Sivir,Bard	Renekton,Trundle,Azir,Jhin,Alistar
Fukuoka SoftBank HAWKS gaming	DetonatioN FocusMe	Fukuoka SoftBank HAWKS gaming	Ambessa,Wukong,Galio,Ezreal,Rakan	Rumble,Nocturne,Orianna,Corki,Braum
Chiefs Esports Club	PSG Talon	PSG Talon	Sion,Maokai,Yone,Lucian,Braum	Ambessa,Jarvan IV,Taliyah,Corki,Alistar
PSG Talon	Chiefs Esports Club	PSG Talon	Gwen,Xin Zhao,Aurora,Varus,Rakan	Rumble,Wukong,Galio,Kai'Sa,Neeko
Team Secret Whales	GAM Esports	GAM Esports	Renekton,Sylas,Azir,Varus,Rell	Gnar,Wukong,Akali,Corki,Nautilus
Team Secret Whales	GAM Esports	GAM Esports	K'Sante,Nocturne,Orianna,Kai'Sa,Rakan	Rumble,Pantheon,Galio,Yunara,Braum
CTBC Flying Oyster	MGN Vikings Esports	CTBC Flying Oyster	Shen,Wukong,Akali,Kai'Sa,Neeko	Sion,Xin Zhao,Orianna,Jhin,Poppy
MGN Vikings Esports	CTBC Flying Oyster	MGN Vikings Esports	Rumble,Vi,Ryze,Senna,Nautilus	K'Sante,Jarvan IV,Viktor,Ezreal,Leona
CTBC Flying Oyster	MGN Vikings Esports	CTBC Flying Oyster	Gwen,Pantheon,Taliyah,Lucian,Braum	Ambessa,Zyra,Corki,Sivir,Rakan
MGN Vikings Esports	PSG Talon	MGN Vikings Esports	Ambessa,Wukong,Annie,Sivir,Braum	Renekton,Xin Zhao,Ryze,Corki,Rell
PSG Talon	MGN Vikings Esports	MGN Vikings Esports	Aatrox,Pantheon,Taliyah,Kai'Sa,Neeko	K'Sante,Jarvan IV,Azir,Senna,Nautilus
GAM Esports	Fukuoka SoftBank HAWKS gaming	GAM Esports	Jax,Zed,Taliyah,Lucian,Braum	Ambessa,Jarvan IV,Ryze,Ezreal,Alistar
GAM Esports	Fukuoka SoftBank HAWKS gaming	GAM Esports	Gwen,Wukong,Annie,Corki,Rakan	Rumble,Xin Zhao,Azir,Jhin,Rell
Team Secret Whales	CTBC Flying Oyster	CTBC Flying Oyster	Jax,Trundle,Ziggs,Jhin,Bard	Ambessa,Xin Zhao,Azir,Varus,Neeko
Team Secret Whales	CTBC Flying Oyster	CTBC Flying Oyster	Aurora,Wukong,Galio,Kai'Sa,Rell	Sion,Pantheon,Annie,Yunara,Braum
DetonatioN FocusMe	Fukuoka SoftBank HAWKS gaming	Fukuoka SoftBank HAWKS gaming	Aatrox,Jarvan IV,Ahri,Xayah,Rakan	Ambessa,Sejuani,Sylas,Kai'Sa,Rell
DetonatioN FocusMe	Fukuoka SoftBank HAWKS gaming	DetonatioN FocusMe	Rumble,Nocturne,Orianna,Corki,Galio	Ornn,Vi,Aurora,Lucian,Braum
DetonatioN FocusMe	Fukuoka SoftBank HAWKS gaming	Fukuoka SoftBank HAWKS gaming	Sion,Xin Zhao,Azir,Senna,Alistar	K'Sante,Wukong,Taliyah,Yunara,Nautilus
PSG Talon	GAM Esports	GAM Esports	Rumble,Vi,Ahri,Corki,Nautilus	Galio,Xin Zhao,Taliyah,Kai'Sa,Braum
PSG Talon	GAM Esports	GAM Esports	Sion,Ivern,Azir,Sivir,Rell	Aurora,Maokai,Yone,Yunara,Rakan
MGN Vikings Esports	Chiefs Esports Club	MGN Vikings Esports	Jayce,Vi,Ziggs,Senna,Nautilus	Ornn,Trundle,Azir,Xayah,Rakan
Chiefs Esports Club	MGN Vikings Esports	Chiefs Esports Club	K'Sante,Maokai,Yone,Kai'Sa,Neeko	Udyr,Jarvan IV,Aurora,Ezreal,Karma
Chiefs Esports Club	MGN Vikings Esports	MGN Vikings Esports	Jax,Xin Zhao,Taliyah,Yunara,Braum	Ambessa,Wukong,Annie,Lucian,Alistar
GAM Esports	Team Secret Whales	Team Secret Whales	K'Sante,Viego,Annie,Varus,Neeko	Renekton,Jarvan IV,Galio,Corki,Bard
Team Secret Whales	GAM Esports	Team Secret Whales	Ornn,Nocturne,Orianna,Kai'Sa,Poppy	Rumble,Trundle,Azir,Sivir,Alistar
Fukuoka SoftBank HAWKS gaming	MGN Vikings Esports	MGN Vikings Esports	Ornn,Pantheon,Viktor,Xayah,Rakan	K'Sante,Jarvan IV,Hwei,Lucian,Nautilus
MGN Vikings Esports	Fukuoka SoftBank HAWKS gaming	MGN Vikings Esports	Ambessa,Zyra,Azir,Senna,Alistar	Yorick,Wukong,Taliyah,Corki,Rell
PSG Talon	CTBC Flying Oyster	CTBC Flying Oyster	Yorick,Trundle,Ryze,Yunara,Lulu	Renekton,Jarvan IV,Aurora,Kai'Sa,Neeko
PSG Talon	CTBC Flying Oyster	CTBC Flying Oyster	Gwen,Skarner,Azir,Sivir,Alistar	Ambessa,Maokai,Yone,Ezreal,Braum
DetonatioN FocusMe	Chiefs Esports Club	DetonatioN FocusMe	Ambessa,Trundle,Orianna,Senna,Blitzcrank	Camille,Ivern,Akali,Xayah,Leona
Chiefs Esports Club	DetonatioN FocusMe	Chiefs Esports Club	K'Sante,Xin Zhao,Galio,Corki,Neeko	Jax,Jarvan IV,Ryze,Sivir,Bard
DetonatioN FocusMe	Chiefs Esports Club	DetonatioN FocusMe	Gwen,Wukong,Ahri,Lucian,Rakan	Rumble,Vi,Taliyah,Kai'Sa,Rell
GAM Esports	CTBC Flying Oyster	CTBC Flying Oyster	Sion,Zyra,Yone,Lucian,Nautilus	Ambessa,Skarner,Twisted Fate,Aphelios,Thresh
CTBC Flying Oyster	GAM Esports	CTBC Flying Oyster	K'Sante,Trundle,Annie,Kai'Sa,Leona	Aurora,Wukong,Ryze,Miss Fortune,Rakan
GAM Esports	CTBC Flying Oyster	GAM Esports	Gwen,Pantheon,Ahri,Sivir,Rell	Gragas,Xin Zhao,Taliyah,Corki,Braum
Fukuoka SoftBank HAWKS gaming	Chiefs Esports Club	Fukuoka SoftBank HAWKS gaming	Yorick,Nocturne,Galio,Kai'Sa,Alistar	Rumble,Xin Zhao,Sylas,Miss Fortune,Blitzcrank
Chiefs Esports Club	Fukuoka SoftBank HAWKS gaming	Chiefs Esports Club	Jax,Ivern,Azir,Xayah,Rakan	Ambessa,Maokai,Yone,Sivir,Nautilus
Fukuoka SoftBank HAWKS gaming	Chiefs Esports Club	Fukuoka SoftBank HAWKS gaming	K'Sante,Wukong,Aurora,Varus,Rell	Sion,Trundle,Ryze,Lucian,Braum
PSG Talon	Team Secret Whales	Team Secret Whales	Rumble,Wukong,Annie,Jhin,Rakan	Sion,Trundle,Ryze,Corki,Bard
PSG Talon	Team Secret Whales	Team Secret Whales	Ambessa,Vi,Taliyah,Vayne,Alistar	Gwen,Xin Zhao,Galio,Sivir,Poppy
DetonatioN FocusMe	MGN Vikings Esports	MGN Vikings Esports	Sion,Xin Zhao,Aurora,Senna,Rakan	Jax,Zyra,Corki,Smolder,Alistar
MGN Vikings Esports	DetonatioN FocusMe	MGN Vikings Esports	K'Sante,Nocturne,Azir,Sivir,Karma	Ornn,Wukong,Taliyah,Varus,Neeko"""

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
