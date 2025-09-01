import csv
import pandas as pd

# Team name to ID mapping
team_meta = pd.read_csv("data/team_meta.csv")
team_to_id = dict(zip(team_meta["name"], team_meta["team_id"]))

# Champion name to ID mapping
champion_name_meta = pd.read_csv("data/champion_meta.csv")
champ_to_id = dict(zip(champion_name_meta["name"], champion_name_meta["champion_id"]))

# Input data with winner column
input_data = """Vivo Keyd Stars	paiN Gaming	Vivo Keyd Stars	Jax,Sejuani,Yone,Kai'Sa,Leona	Yorick,Maokai,Ryze,Ezreal,Braum
Vivo Keyd Stars	paiN Gaming	Vivo Keyd Stars	K'Sante,Xin Zhao,Aurora,Zeri,Renata Glasc	Renekton,Zyra,Taliyah,Sivir,Alistar
Vivo Keyd Stars	paiN Gaming	Vivo Keyd Stars	Ambessa,Jarvan IV,Azir,Yunara,Rakan	Camille,Trundle,Ziggs,Corki,Neeko
paiN Gaming	Vivo Keyd Stars	paiN Gaming	Galio,Nocturne,Orianna,Varus,Nautilus	Rumble,Wukong,Akali,Jhin,Rell
FURIA	LOUD	LOUD	Sion,Vi,Galio,Ashe,Seraphine	Cho'Gath,Volibear,Ryze,Lucian,Rell
FURIA	LOUD	LOUD	K'Sante,Xin Zhao,Azir,Jhin,Bard	Renekton,Skarner,Ziggs,Corki,Pyke
FURIA	LOUD	LOUD	Gwen,Pantheon,Annie,Yunara,Neeko	Rumble,Wukong,Orianna,Sivir,Alistar
Leviatan	RED Canids	RED Canids	Aatrox,Vi,Ryze,Lucian,Nami	Yorick,Skarner,Syndra,Kalista,Neeko
RED Canids	Leviatan	RED Canids	Sion,Nidalee,Zed,Miss Fortune,Pyke	K'Sante,Sejuani,Taliyah,Ezreal,Rakan
Leviatan	RED Canids	Leviatan	Ambessa,Poppy,Ziggs,Varus,Nautilus	Renekton,Wukong,Azir,Jhin,Rell
RED Canids	Leviatan	RED Canids	Galio,Xin Zhao,Ahri,Yunara,Alistar	Rumble,Jarvan IV,Orianna,Xayah,Bard
Leviatan	Isurus	Leviatan	Renekton,Maokai,Yone,Aphelios,Lulu	Cho'Gath,Amumu,Jayce,Kalista,Renata Glasc
Leviatan	Isurus	Leviatan	Jax,Skarner,Aurora,Yunara,Bard	Gangplank,Jarvan IV,Taliyah,Zeri,Karma
Isurus	Leviatan	Isurus	Sion,Xin Zhao,Ahri,Varus,Leona	K'Sante,Pantheon,Akali,Corki,Neeko
Leviatan	Isurus	Leviatan	Rumble,Trundle,Syndra,Xayah,Rell	Galio,Zed,Annie,Sivir,Rakan
Isurus	Leviatan	Isurus	Ambessa,Wukong,Viktor,Lucian,Alistar	Gwen,Vi,Orianna,Kai'Sa,Nautilus
LOUD	Fluxo W7M	LOUD	Renekton,Volibear,Orianna,Aphelios,Rell	Jax,Skarner,Akali,Ezreal,Bard
Fluxo W7M	LOUD	LOUD	Galio,Xin Zhao,Ahri,Kai'Sa,Braum	Rumble,Viego,Syndra,Sivir,Alistar
LOUD	Fluxo W7M	LOUD	Gwen,Trundle,Ryze,Xayah,Rakan	Aurora,Jarvan IV,Annie,Corki,Nautilus
paiN Gaming	RED Canids	paiN Gaming	Aatrox,Vi,Taliyah,Senna,Nautilus	Aurora,Dr. Mundo,Lucian,Miss Fortune,Leona
RED Canids	paiN Gaming	paiN Gaming	Yorick,Skarner,Twisted Fate,Kalista,Renata Glasc	Renekton,Zyra,Annie,Xayah,Rakan
RED Canids	paiN Gaming	RED Canids	Sion,Xin Zhao,Ryze,Yunara,Karma	Cho'Gath,Maokai,Corki,Kai'Sa,Neeko
paiN Gaming	RED Canids	paiN Gaming	Rumble,Trundle,Azir,Varus,Alistar	Ambessa,Nocturne,Orianna,Ezreal,Bard
FURIA	Vivo Keyd Stars	Vivo Keyd Stars	K'Sante,Viego,Ryze,Aphelios,Tahm Kench	Camille,Nocturne,Galio,Jinx,Thresh
FURIA	Vivo Keyd Stars	Vivo Keyd Stars	Jax,Jarvan IV,Aurora,Senna,Nautilus	Ambessa,Sejuani,Azir,Sivir,Neeko
Vivo Keyd Stars	FURIA	Vivo Keyd Stars	Sion,Pantheon,Annie,Yunara,Rell	Rumble,Skarner,Taliyah,Corki,Rakan
RED Canids	paiN Gaming	RED Canids	Rumble,Xin Zhao,Sylas,Varus,Rakan	Ambessa,Trundle,Galio,Sivir,Bard
paiN Gaming	RED Canids	RED Canids	K'Sante,Jarvan IV,Taliyah,Yunara,Rell	Cho'Gath,Wukong,Akali,Corki,Neeko
Fluxo W7M	Leviatan	Leviatan	Sion,Xin Zhao,Viktor,Ezreal,Leona	K'Sante,Vi,Ryze,Corki,Rakan
Fluxo W7M	Leviatan	Leviatan	Ambessa,Trundle,Azir,Senna,Rell	Renekton,Nocturne,Orianna,Sivir,Nautilus
Isurus	LOUD	LOUD	Cho'Gath,Trundle,Aurora,Varus,Bard	Yorick,Ambessa,Annie,Lucian,Pyke
LOUD	Isurus	LOUD	Rumble,Wukong,Orianna,Sivir,Alistar	Sion,Vi,Taliyah,Yunara,Nautilus
Vivo Keyd Stars	FURIA	FURIA	Sion,Pantheon,Annie,Miss Fortune,Alistar	K'Sante,Skarner,Akali,Corki,Neeko
Vivo Keyd Stars	FURIA	Vivo Keyd Stars	Ambessa,Trundle,Galio,Varus,Nautilus	Rumble,Vi,Ahri,Sivir,Braum
Vivo Keyd Stars	FURIA	FURIA	Gwen,Jarvan IV,Viktor,Kai'Sa,Rell	Aurora,Xin Zhao,Ryze,Yunara,Renata Glasc
RED Canids	LOUD	RED Canids	Galio,Pantheon,Sylas,Corki,Leona	Rumble,Jarvan IV,Yone,Jhin,Nautilus
LOUD	RED Canids	LOUD	Ambessa,Volibear,Aurora,Kai'Sa,Rell	Aatrox,Vi,Annie,Senna,Alistar
LOUD	RED Canids	RED Canids	Renekton,Xin Zhao,Orianna,Xayah,Rakan	Yorick,Wukong,Taliyah,Ezreal,Bard
Leviatan	Vivo Keyd Stars	Vivo Keyd Stars	Ambessa,Vi,Akali,Sivir,Neeko	Rumble,Xin Zhao,Sylas,Jhin,Alistar
Leviatan	Vivo Keyd Stars	Vivo Keyd Stars	Gwen,Trundle,Ryze,Senna,Nautilus	Jax,Wukong,Orianna,Corki,Rell
Isurus	Fluxo W7M	Isurus	Yorick,Vi,Viktor,Sivir,Alistar	Jax,Sejuani,Sylas,Corki,Rell
Fluxo W7M	Isurus	Fluxo W7M	Renekton,Pantheon,Ryze,Ashe,Seraphine	K'Sante,Poppy,Aurora,Lucian,Blitzcrank
Fluxo W7M	Isurus	Isurus	Ambessa,Wukong,Annie,Yunara,Nautilus	Sion,Xin Zhao,Azir,Xayah,Rakan
FURIA	paiN Gaming	paiN Gaming	Gangplank,Vi,Aurora,Senna,Nautilus	Jax,Skarner,Orianna,Lucian,Nami
FURIA	paiN Gaming	paiN Gaming	Sion,Poppy,Azir,Kai'Sa,Alistar	Rumble,Jarvan IV,Ziggs,Miss Fortune,Rakan
paiN Gaming	FURIA	FURIA	Gwen,Xin Zhao,Ryze,Sivir,Neeko	Ambessa,Wukong,Zoe,Varus,Karma
LOUD	Vivo Keyd Stars	Vivo Keyd Stars	Sion,Sejuani,Viktor,Ezreal,Bard	K'Sante,Nocturne,Sylas,Kai'Sa,Neeko
Vivo Keyd Stars	LOUD	Vivo Keyd Stars	Gwen,Jarvan IV,Aurora,Jhin,Alistar	Gragas,Ambessa,Orianna,Senna,Braum
LOUD	Vivo Keyd Stars	LOUD	Yorick,Wukong,Annie,Sivir,Rakan	Rumble,Xin Zhao,Taliyah,Corki,Rell
RED Canids	Isurus	RED Canids	Ambessa,Xin Zhao,Twisted Fate,Senna,Rell	Aatrox,Lee Sin,Annie,Smolder,Nautilus
RED Canids	Isurus	Isurus	Yorick,Sejuani,Azir,Caitlyn,Neeko	Sion,Jarvan IV,Viktor,Sivir,Alistar
Isurus	RED Canids	RED Canids	Rumble,Wukong,Taliyah,Jhin,Rakan	Renekton,Trundle,Orianna,Ezreal,Leona
Leviatan	paiN Gaming	paiN Gaming	K'Sante,Vi,Ahri,Kai'Sa,Rell	Jax,Nocturne,Galio,Corki,Rakan
paiN Gaming	Leviatan	paiN Gaming	Rumble,Maokai,Yone,Miss Fortune,Alistar	Sion,Xin Zhao,Azir,Sivir,Braum
Fluxo W7M	FURIA	FURIA	Rumble,Xin Zhao,Ahri,Kai'Sa,Rell	Ornn,Jax,Sylas,Senna,Seraphine
FURIA	Fluxo W7M	FURIA	Gwen,Trundle,Azir,Jhin,Rakan	Aurora,Wukong,Akali,Ashe,Alistar"""

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
