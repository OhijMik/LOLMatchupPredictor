import csv
import pandas as pd

# Team name to ID mapping
team_meta = pd.read_csv("data/team_meta.csv")
team_to_id = dict(zip(team_meta["name"], team_meta["team_id"]))

# Champion name to ID mapping
champion_name_meta = pd.read_csv("data/champion_meta.csv")
champ_to_id = dict(zip(champion_name_meta["name"], champion_name_meta["champion_id"]))

# Input data with winner column
input_data = """T1	Gen.G	Gen.G	Renekton,Viego,Ahri,Caitlyn,Karma	Aatrox,Nidalee,Aurora,Miss Fortune,Pyke
Gen.G	T1	Gen.G	Jayce,Trundle,Viktor,Zeri,Rakan	K'Sante,Skarner,Hwei,Jinx,Tahm Kench
T1	Gen.G	T1	Ornn,Nocturne,Azir,Xayah,Renata Glasc	Rumble,Xin Zhao,Annie,Sivir,Rell
Gen.G	T1	Gen.G	Sion,Vi,Ryze,Senna,Nautilus	Camille,Wukong,Galio,Corki,Poppy
Gen.G	T1	T1	Jax,Sejuani,Taliyah,Lucian,Braum	Gwen,Jarvan IV,Orianna,Jhin,Alistar
Anyone's Legend	T1	T1	Aatrox,Olaf,Twisted Fate,Ziggs,Poppy	Gragas,Skarner,Hwei,Jinx,Alistar
T1	Anyone's Legend	T1	Jax,Lillia,Corki,Xayah,Rakan	Ambessa,Maokai,Sylas,Senna,Tahm Kench
Anyone's Legend	T1	Anyone's Legend	Rumble,Xin Zhao,Viktor,Varus,Leona	Ornn,Jarvan IV,Aurora,Miss Fortune,Neeko
T1	Anyone's Legend	T1	Renekton,Lee Sin,Ryze,Lucian,Braum	Yorick,Trundle,Orianna,Ezreal,Karma
T1	Anyone's Legend	Anyone's Legend	Gwen,Vi,Galio,Jhin,Nautilus	Jayce,Wukong,Annie,Kai'Sa,Rell
Bilibili Gaming	Anyone's Legend	Anyone's Legend	Fiora,Skarner,Akali,Varus,Renata Glasc	Gwen,Vi,Annie,Sivir,Blitzcrank
Bilibili Gaming	Anyone's Legend	Anyone's Legend	Rumble,Nocturne,Aurora,Ezreal,Rell	Sion,Jarvan IV,Ryze,Lucian,Braum
Anyone's Legend	Bilibili Gaming	Anyone's Legend	Yorick,Wukong,Taliyah,Jhin,Bard	Jax,Trundle,Azir,Corki,Neeko
Gen.G	T1	Gen.G	Renekton,Nidalee,Aurora,Jinx,Tahm Kench	Ambessa,Lee Sin,Sylas,Draven,Pyke
T1	Gen.G	T1	Gragas,Nocturne,Orianna,Corki,Karma	Poppy,Zed,Ahri,Kalista,Renata Glasc
Gen.G	T1	Gen.G	K'Sante,Pantheon,Galio,Senna,Alistar	Sion,Xin Zhao,Viktor,Miss Fortune,Bard
T1	Gen.G	T1	Ornn,Jarvan IV,Taliyah,Lucian,Braum	Rumble,Skarner,Ryze,Ezreal,Rell
T1	Gen.G	Gen.G	Jax,Sejuani,Azir,Xayah,Rakan	Gwen,Wukong,Annie,Jhin,Neeko
Bilibili Gaming	FlyQuest	Bilibili Gaming	Rumble,Nocturne,Galio,Ashe,Shen	Urgot,Lee Sin,Zilean,Lucian,Leona
Bilibili Gaming	FlyQuest	FlyQuest	Yorick,Maokai,Tristana,Varus,Rakan	Sett,Trundle,Hwei,Jhin,Bard
Bilibili Gaming	FlyQuest	Bilibili Gaming	Ambessa,Vi,Ahri,Kai'Sa,Nautilus	Gangplank,Poppy,Ryze,Senna,Alistar
Bilibili Gaming	FlyQuest	Bilibili Gaming	Ornn,Pantheon,Viktor,Corki,Rell	Renekton,Wukong,Annie,Kalista,Renata Glasc
FlyQuest	Bilibili Gaming	FlyQuest	Aatrox,Sejuani,Taliyah,Ezreal,Karma	Sion,Xin Zhao,Aurora,Miss Fortune,Neeko
Anyone's Legend	CTBC Flying Oyster	Anyone's Legend	Jayce,Maokai,Sylas,Jinx,Blitzcrank	K'Sante,Jarvan IV,Aurora,Sivir,Thresh
Anyone's Legend	CTBC Flying Oyster	CTBC Flying Oyster	Gwen,Lee Sin,Annie,Xayah,Rell	Gnar,Trundle,Orianna,Ezreal,Braum
CTBC Flying Oyster	Anyone's Legend	Anyone's Legend	Rumble,Skarner,Corki,Kai'Sa,Nautilus	Galio,Wukong,Ryze,Lucian,Neeko
CTBC Flying Oyster	Anyone's Legend	Anyone's Legend	Gragas,Xin Zhao,Taliyah,Miss Fortune,Alistar	Yorick,Poppy,Azir,Jhin,Bard
Bilibili Gaming	T1	T1	Ambessa,Vi,Ahri,Xayah,Gragas	Renekton,Skarner,Ryze,Varus,Alistar
Bilibili Gaming	T1	T1	Rumble,Wukong,Annie,Ezreal,Rell	Ornn,Xin Zhao,Viktor,Caitlyn,Braum
Bilibili Gaming	T1	T1	Sion,Poppy,Taliyah,Kalista,Renata Glasc	Yorick,Pantheon,Orianna,Jhin,Neeko
CTBC Flying Oyster	Movistar KOI	CTBC Flying Oyster	K'Sante,Pantheon,Viktor,Aphelios,Thresh	Renekton,Vi,Aurelion Sol,Kalista,Renata Glasc
Movistar KOI	CTBC Flying Oyster	Movistar KOI	Irelia,Poppy,Taliyah,Xayah,Rell	Yorick,Nocturne,Aurora,Kai'Sa,Rakan
Movistar KOI	CTBC Flying Oyster	CTBC Flying Oyster	Ambessa,Lee Sin,Twisted Fate,Caitlyn,Karma	Shen,Skarner,Ryze,Jhin,Bard
CTBC Flying Oyster	Movistar KOI	CTBC Flying Oyster	Sion,Xin Zhao,Azir,Ezreal,Leona	Rumble,Trundle,Yone,Sivir,Alistar
Gen.G	Anyone's Legend	Gen.G	Camille,Sejuani,Ryze,Xayah,Blitzcrank	Gragas,Skarner,Cassiopeia,Corki,Shen
Anyone's Legend	Gen.G	Anyone's Legend	Smolder,Jarvan IV,Galio,Miss Fortune,Neeko	K'Sante,Naafiri,Sylas,Caitlyn,Karma
Anyone's Legend	Gen.G	Gen.G	Sion,Trundle,Akali,Varus,Bard	Ambessa,Vi,Taliyah,Ziggs,Rakan
Gen.G	Anyone's Legend	Gen.G	Gwen,Nocturne,Azir,Senna,Nautilus	Jax,Poppy,Twisted Fate,Ezreal,Braum
Anyone's Legend	Gen.G	Anyone's Legend	Rumble,Pantheon,Annie,Kai'Sa,Rell	Ornn,Xin Zhao,Aurora,Jhin,Alistar
FlyQuest	G2 Esports	FlyQuest	Yorick,Trundle,Orianna,Kai'Sa,Neeko	Cho'Gath,Naafiri,Akali,Lucian,Nautilus
G2 Esports	FlyQuest	FlyQuest	K'Sante,Vi,Aurora,Corki,Rell	Garen,Wukong,Annie,Senna,Bard
FlyQuest	G2 Esports	FlyQuest	Sion,Pantheon,Ryze,Varus,Karma	Aatrox,Maokai,Cassiopeia,Jhin,Alistar
CTBC Flying Oyster	T1	T1	Ornn,Zyra,Tristana,Xayah,Rakan	Jayce,Sejuani,Orianna,Jinx,Tahm Kench
T1	CTBC Flying Oyster	T1	Rumble,Jarvan IV,Sylas,Varus,Poppy	Ambessa,Skarner,Cassiopeia,Jhin,Nautilus
T1	CTBC Flying Oyster	CTBC Flying Oyster	Gwen,Zed,Galio,Senna,Thresh	Gragas,Trundle,Swain,Caitlyn,Braum
CTBC Flying Oyster	T1	CTBC Flying Oyster	K'Sante,Vi,Aurora,Lucian,Nami	Jax,Wukong,Ryze,Kalista,Renata Glasc
CTBC Flying Oyster	T1	T1	Sion,Pantheon,Viktor,Ezreal,Leona	Aatrox,Xin Zhao,Annie,Corki,Neeko
Movistar KOI	Bilibili Gaming	Bilibili Gaming	Ambessa,Sejuani,Ryze,Kalista,Renata Glasc	K'Sante,Skarner,Syndra,Ashe,Neeko
Bilibili Gaming	Movistar KOI	Bilibili Gaming	Sion,Vi,Sylas,Caitlyn,Elise	Aatrox,Naafiri,Ahri,Ezreal,Nautilus
Movistar KOI	Bilibili Gaming	Movistar KOI	Akali,Wukong,Azir,Kai'Sa,Rell	Gwen,Xin Zhao,Viktor,Corki,Leona
Movistar KOI	Bilibili Gaming	Bilibili Gaming	Galio,Maokai,Yone,Varus,Alistar	Rumble,Pantheon,Aurora,Miss Fortune,Rakan
Anyone's Legend	FlyQuest	Anyone's Legend	Ambessa,Poppy,Aurora,Lucian,Leona	Shen,Lee Sin,Ahri,Ziggs,Nautilus
FlyQuest	Anyone's Legend	Anyone's Legend	Cho'Gath,Viego,Twisted Fate,Jhin,Alistar	Sion,Wukong,Azir,Varus,Braum
Anyone's Legend	FlyQuest	Anyone's Legend	Yorick,Trundle,Ryze,Corki,Neeko	Mordekaiser,Vi,Viktor,Kalista,Renata Glasc
Anyone's Legend	FlyQuest	FlyQuest	Rumble,Xin Zhao,Taliyah,Xayah,Rakan	Galio,Pantheon,Orianna,Senna,Rell
Gen.G	G2 Esports	Gen.G	Jayce,Skarner,Taliyah,Corki,Poppy	Aatrox,Dr. Mundo,Twisted Fate,Kai'Sa,Leona
G2 Esports	Gen.G	Gen.G	Gnar,Jarvan IV,Viktor,Ezreal,Rell	K'Sante,Lee Sin,Orianna,Miss Fortune,Nautilus
Gen.G	G2 Esports	Gen.G	Rumble,Vi,Aurora,Jhin,Alistar	Galio,Wukong,Ryze,Senna,Tahm Kench
Gen.G	G2 Esports	G2 Esports	Renekton,Xin Zhao,Azir,Lucian,Braum	Jax,Maokai,Yone,Varus,Rakan
G2 Esports	GAM Esports	G2 Esports	K'Sante,Viego,Annie,Senna,Tahm Kench	Aatrox,Vi,Orianna,Kalista,Seraphine
G2 Esports	GAM Esports	GAM Esports	Cho'Gath,Naafiri,Twisted Fate,Kai'Sa,Leona	Sion,Lillia,Sylas,Caitlyn,Galio
GAM Esports	G2 Esports	GAM Esports	Jax,Wukong,Ahri,Xayah,Rakan	Ambessa,Nunu & Willump,Tristana,Miss Fortune,Neeko
GAM Esports	G2 Esports	G2 Esports	Jayce,Pantheon,Hwei,Corki,Nautilus	Gragas,Poppy,Ryze,Lucian,Braum
G2 Esports	GAM Esports	G2 Esports	Renekton,Trundle,Syndra,Varus,Alistar	Gnar,Xin Zhao,Taliyah,Jhin,Rell
G2 Esports	Bilibili Gaming	Bilibili Gaming	Olaf,Trundle,Twisted Fate,Senna,Rell	Renekton,Poppy,Veigar,Kai'Sa,Rakan
G2 Esports	Bilibili Gaming	Bilibili Gaming	Jax,Vi,Ahri,Sivir,Neeko	Sion,Skarner,Taliyah,Varus,Karma
Bilibili Gaming	G2 Esports	Bilibili Gaming	Rumble,Xin Zhao,Annie,Miss Fortune,Alistar	Ornn,Pantheon,Aurora,Ezreal,Leona
FURIA	GAM Esports	GAM Esports	Gnar,Trundle,Kassadin,Ezreal,Karma	Gangplank,Naafiri,Orianna,Kai'Sa,Bard
FURIA	GAM Esports	GAM Esports	Renekton,Skarner,Azir,Yasuo,Alistar	K'Sante,Viego,LeBlanc,Lucian,Braum
GAM Esports	FURIA	FURIA	Aatrox,Kha'Zix,Twisted Fate,Kalista,Neeko	Ambessa,Poppy,Sylas,Ashe,Seraphine
GAM Esports	FURIA	FURIA	Gwen,Vi,Aurora,Jhin,Nautilus	Jax,Wukong,Annie,Corki,Leona
GAM Esports	FURIA	GAM Esports	Rumble,Pantheon,Taliyah,Xayah,Rakan	Galio,Xin Zhao,Ahri,Smolder,Rell
GAM Esports	Bilibili Gaming	Bilibili Gaming	Yorick,Jarvan IV,Viktor,Miss Fortune,Neeko	Renekton,Xin Zhao,Aurora,Caitlyn,Karma
GAM Esports	Bilibili Gaming	Bilibili Gaming	Sion,Vi,Ahri,Tristana,Rakan	Aatrox,Wukong,Annie,Ezreal,Rell
Bilibili Gaming	GAM Esports	Bilibili Gaming	Ambessa,Poppy,Taliyah,Jhin,Alistar	Rumble,Maokai,Corki,Varus,Nautilus
G2 Esports	FURIA	G2 Esports	Gragas,Jarvan IV,Yone,Senna,Braum	Gnar,Lillia,Jayce,Ziggs,Leona
G2 Esports	FURIA	FURIA	Renekton,Naafiri,Neeko,Kalista,Blitzcrank	Sion,Nocturne,Akali,Ashe,Seraphine
FURIA	G2 Esports	G2 Esports	Rumble,Pantheon,Orianna,Lucian,Nami	Ornn,Trundle,Annie,Jhin,Nautilus
G2 Esports	FURIA	G2 Esports	Jax,Maokai,Corki,Varus,Alistar	K'Sante,Wukong,Ryze,Ezreal,Rell
FURIA	G2 Esports	FURIA	Aatrox,Xin Zhao,Taliyah,Nilah,Rakan	Warwick,Vi,Ahri,Kai'Sa,Poppy"""

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
