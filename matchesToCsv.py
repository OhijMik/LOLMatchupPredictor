import csv

# Team name to ID mapping
team_to_id = {
    "BNK FEARX": 24,
    "OKSavingsBank BRION": 22,
    "OK BRION": 22,
    "DN Freecs": 23,
    "KT Rolster": 27,
    "T1": 20,
    "DRX": 28,
    "Gen.G": 26,
    "Dplus KIA": 25,
    "Nongshim RedForce": 29,
    "NS RedForce": 29,
    "Hanwha Life Esports": 21,
    "Hanwha Life": 21
}

# Champion name to ID mapping (from champion_meta)
champ_to_id = {
    "Aatrox": 1, "Ahri": 2, "Akali": 3, "Akshan": 4, "Alistar": 5, "Ambessa": 6, "Amumu": 7, "Anivia": 8, "Annie": 9,
    "Aphelios": 10, "Ashe": 11, "Aurelion Sol": 12, "Aurora": 13, "Azir": 14, "Bard": 15, "Bel'Veth": 16, "Blitzcrank": 17,
    "Brand": 18, "Braum": 19, "Briar": 20, "Caitlyn": 21, "Camille": 22, "Cassiopeia": 23, "Cho'Gath": 24, "Corki": 25,
    "Darius": 26, "Diana": 27, "Dr. Mundo": 28, "Draven": 29, "Ekko": 30, "Elise": 31, "Evelynn": 32, "Ezreal": 33,
    "Fiddlesticks": 34, "Fiora": 35, "Fizz": 36, "Galio": 37, "Gangplank": 38, "Garen": 39, "Gnar": 40, "Gragas": 41,
    "Graves": 42, "Gwen": 43, "Hecarim": 44, "Heimerdinger": 45, "Hwei": 46, "Illaoi": 47, "Irelia": 48, "Ivern": 49,
    "Janna": 50, "Jarvan IV": 51, "Jax": 52, "Jayce": 53, "Jhin": 54, "Jinx": 55, "K'Sante": 56, "Kai'Sa": 57,
    "Kalista": 58, "Karma": 59, "Karthus": 60, "Kassadin": 61, "Katarina": 62, "Kayle": 63, "Kayn": 64, "Kennen": 65,
    "Kha'Zix": 66, "Kindred": 67, "Kled": 68, "Kog'Maw": 69, "LeBlanc": 70, "Lee Sin": 71, "Leona": 72, "Lillia": 73,
    "Lissandra": 74, "Lucian": 75, "Lulu": 76, "Lux": 77, "Malphite": 78, "Malzahar": 79, "Maokai": 80, "Master Yi": 81,
    "Mel": 82, "Milio": 83, "Miss Fortune": 84, "Mordekaiser": 85, "Morgana": 86, "Naafiri": 87, "Nami": 88, "Nasus": 89,
    "Nautilus": 90, "Neeko": 91, "Nidalee": 92, "Nilah": 93, "Nocturne": 94, "Nunu & Willump": 95, "Olaf": 96, "Orianna": 97,
    "Ornn": 98, "Pantheon": 99, "Poppy": 100, "Pyke": 101, "Qiyana": 102, "Quinn": 103, "Rakan": 104, "Rammus": 105,
    "Rek'Sai": 106, "Rell": 107, "Renata Glasc": 108, "Renekton": 109, "Rengar": 110, "Riven": 111, "Rumble": 112,
    "Ryze": 113, "Samira": 114, "Sejuani": 115, "Senna": 116, "Seraphine": 117, "Sett": 118, "Shaco": 119, "Shen": 120,
    "Shyvana": 121, "Singed": 122, "Sion": 123, "Sivir": 124, "Skarner": 125, "Smolder": 126, "Sona": 127, "Soraka": 128,
    "Swain": 129, "Sylas": 130, "Syndra": 131, "Tahm Kench": 132, "Taliyah": 133, "Talon": 134, "Taric": 135, "Teemo": 136,
    "Thresh": 137, "Tristana": 138, "Trundle": 139, "Tryndamere": 140, "Twisted Fate": 141, "Twitch": 142, "Udyr": 143,
    "Urgot": 144, "Varus": 145, "Vayne": 146, "Veigar": 147, "Vel'Koz": 148, "Vex": 149, "Vi": 150, "Viego": 151,
    "Viktor": 152, "Vladimir": 153, "Volibear": 154, "Warwick": 155, "Wukong": 156, "Xayah": 157, "Xerath": 158,
    "Xin Zhao": 159, "Yasuo": 160, "Yone": 161, "Yorick": 162, "Yunara": 163, "Yuumi": 164, "Zac": 165, "Zed": 166,
    "Zeri": 167, "Ziggs": 168, "Zilean": 169, "Zoe": 170, "Zyra": 171
}

input_text = """BNK FEARX	OKSavingsBank BRION	Rumble,Naafiri,Annie,Ezreal,Leona	Gwen,Wukong,Ahri,Varus,Braum
OKSavingsBank BRION	DN Freecs	Aatrox,Naafiri,Viktor,Miss Fortune,Poppy	Renekton,Lillia,Hwei,Ezreal,Alistar
DN Freecs	OKSavingsBank BRION	Rumble,Wukong,Ahri,Xayah,Rell	Yorick,Nocturne,Aurora,Zeri,Rakan
DN Freecs	OKSavingsBank BRION	Jayce,Pantheon,Azir,Kai'Sa,Neeko	Sion,Xin Zhao,Taliyah,Ashe,Braum
KT Rolster	T1	Aatrox,Sejuani,Hwei,Kalista,Elise	Renekton,Vi,Viktor,Ashe,Renata Glasc
KT Rolster	T1	Galio,Viego,Azir,Jhin,Rell	Rumble,Xin Zhao,Ahri,Lucian,Braum
BNK FEARX	DRX	Jayce,Skarner,Ahri,Lucian,Milio	Sion,Viego,Taliyah,Ezreal,Rell
DRX	BNK FEARX	Gwen,Naafiri,Aurora,Jhin,Nautilus	Rumble,Xin Zhao,Azir,Kai'Sa,Leona
Gen.G	Dplus KIA	Gwen,Skarner,Corki,Kai'Sa,Leona	Jayce,Sejuani,Ryze,Ashe,Renata Glasc
Gen.G	Dplus KIA	Rumble,Naafiri,Taliyah,Jhin,Rell	Ornn,Xin Zhao,Azir,Miss Fortune,Alistar
Nongshim RedForce	Hanwha Life Esports	Ambessa,Xin Zhao,Ahri,Zeri,Alistar	Nidalee,Maokai,Yone,Xayah,Rakan
Hanwha Life Esports	Nongshim RedForce	Jayce,Sejuani,Taliyah,Varus,Pantheon	Gwen,Skarner,Ryze,Caitlyn,Elise
DN Freecs	T1	Jax,Viego,Ryze,Varus,Rell	Gnar,Pantheon,Viktor,Jhin,Leona
T1	DN Freecs	Rumble,Xin Zhao,Azir,Xayah,Rakan	Gwen,Naafiri,Orianna,Tristana,Alistar
DRX	OKSavingsBank BRION	Jayce,Poppy,Viktor,Caitlyn,Elise	Ambessa,Sejuani,Orianna,Jinx,Rakan
OKSavingsBank BRION	DRX	Sion,Wukong,Ahri,Varus,Braum	Renekton,Lillia,Ryze,Miss Fortune,Rell
OKSavingsBank BRION	DRX	Rumble,Xin Zhao,Azir,Jhin,Nautilus	Aurora,Nocturne,Taliyah,Kalista,Alistar
KT Rolster	Gen.G	Rumble,Lillia,Yone,Ezreal,Rell	Ryze,Skarner,Viktor,Ashe,Braum
Gen.G	KT Rolster	Jayce,Xin Zhao,Taliyah,Xayah,Rakan	Sion,Naafiri,Azir,Jhin,Poppy
BNK FEARX	Hanwha Life Esports	Jax,Skarner,Viktor,Kalista,Neeko	Kennen,Poppy,Sylas,Ashe,Renata Glasc
BNK FEARX	Hanwha Life Esports	Jayce,Sejuani,Taliyah,Kai'Sa,Alistar	Gwen,Xin Zhao,Ryze,Varus,Rakan
Dplus KIA	Nongshim RedForce	Gwen,Skarner,Syndra,Ezreal,Bard	Ambessa,Lillia,Sylas,Miss Fortune,Lulu
Nongshim RedForce	Dplus KIA	Jayce,Poppy,Taliyah,Varus,Elise	Yorick,Wukong,Ahri,Kalista,Neeko
Nongshim RedForce	Dplus KIA	Rumble,Sejuani,Yone,Kai'Sa,Nautilus	Aurora,Xin Zhao,Ryze,Xayah,Alistar
Dplus KIA	Hanwha Life Esports	Sion,Viego,Viktor,Miss Fortune,Leona	Gnar,Wukong,Taliyah,Jhin,Alistar
Hanwha Life Esports	Dplus KIA	Jax,Sejuani,Yone,Kalista,Gragas	Renekton,Nidalee,Pantheon,Corki,Braum
Dplus KIA	Hanwha Life Esports	Ambessa,Poppy,Azir,Ezreal,Rell	Rumble,Naafiri,Ahri,Varus,Nautilus
OKSavingsBank BRION	T1	Yorick,Wukong,Taliyah,Miss Fortune,Nautilus	Sion,Viego,Galio,Lucian,Alistar
T1	OKSavingsBank BRION	Gwen,Pantheon,Sylas,Xayah,Elise	Ambessa,Naafiri,Ahri,Ezreal,Rell
OKSavingsBank BRION	T1	Rumble,Sejuani,Yone,Jhin,Rakan	Aurora,Skarner,Viktor,Varus,Poppy
DRX	Gen.G	Yorick,Lillia,Ryze,Varus,Braum	Renekton,Nidalee,Galio,Miss Fortune,Alistar
DRX	Gen.G	Jayce,Skarner,Azir,Ezreal,Leona	Rumble,Naafiri,Ahri,Jhin,Poppy
DN Freecs	BNK FEARX	Gragas,Naafiri,Orianna,Miss Fortune,Rakan	Jax,Pantheon,Viktor,Lucian,Alistar
BNK FEARX	DN Freecs	Renekton,Lillia,Ryze,Kalista,Ashe	K'Sante,Skarner,Ahri,Draven,Renata Glasc
DN Freecs	BNK FEARX	Ambessa,Xin Zhao,Taliyah,Kai'Sa,Neeko	Jayce,Poppy,Azir,Ezreal,Karma
T1	Dplus KIA	Renekton,Lillia,Viktor,Lucian,Braum	Aatrox,Pantheon,Sylas,Ashe,Poppy
Dplus KIA	T1	Gwen,Viego,Ahri,Miss Fortune,Rell	Jayce,Sejuani,Yone,Xayah,Rakan
T1	Dplus KIA	Ornn,Naafiri,Azir,Jhin,Neeko	Rumble,Skarner,Taliyah,Varus,Leona
KT Rolster	Nongshim RedForce	Jayce,Pantheon,Ahri,Kai'Sa,Rakan	Nidalee,Xin Zhao,Taliyah,Ashe,Leona
KT Rolster	Nongshim RedForce	Rumble,Lillia,Corki,Kalista,Neeko	Anivia,Sejuani,Yone,Ezreal,Elise
OKSavingsBank BRION	Hanwha Life Esports	Jax,Xin Zhao,Akali,Lucian,Braum	Renekton,Nidalee,Yone,Kai'Sa,Neeko
Hanwha Life Esports	OKSavingsBank BRION	Jayce,Poppy,Azir,Xayah,Rakan	Rumble,Naafiri,Ahri,Jhin,Nautilus
DN Freecs	Gen.G	Jayce,Xin Zhao,Ahri,Zeri,Lulu	Rumble,Pantheon,Sylas,Xayah,Blitzcrank
Gen.G	DN Freecs	Gwen,Naafiri,Taliyah,Jhin,Nautilus	Ambessa,Sejuani,Azir,Ezreal,Braum
BNK FEARX	Nongshim RedForce	Sion,Naafiri,Taliyah,Ezreal,Rell	Nidalee,Poppy,Azir,Kai'Sa,Leona
Nongshim RedForce	BNK FEARX	Gwen,Xin Zhao,Ryze,Zeri,Alistar	Rumble,Skarner,Yone,Varus,Renata Glasc
DRX	KT Rolster	Ambessa,Skarner,Aurora,Ezreal,Bard	Aatrox,Lillia,Taliyah,Varus,Rell
DRX	KT Rolster	Jayce,Naafiri,Ahri,Xayah,Rakan	Rumble,Xin Zhao,Ryze,Miss Fortune,Poppy
DN Freecs	KT Rolster	Ambessa,Naafiri,Ryze,Jhin,Leona	Jayce,Fiddlesticks,Aurora,Ezreal,Poppy
KT Rolster	DN Freecs	Galio,Xin Zhao,Ahri,Kalista,Neeko	Rumble,Skarner,Taliyah,Xayah,Rakan"""

# Split into lines and format as list
matches = []
for line in input_text.split('\n'):
    if line.strip():  # Skip empty lines
        # Escape quotes and format as string
        formatted_line = line.replace('\t', '\\t')
        matches.append(f'"{formatted_line}"')

# Create the final list
matches_list = "[\n" + ",\n".join(matches) + "\n]"

# Create CSV files
blue_team_data = []
red_team_data = []

for match in matches_list:
    parts = match.split('\t')
    blue_team = parts[0]
    red_team = parts[1]
    blue_draft = parts[2].split(',')
    red_draft = parts[3].split(',')

    # Convert champion names to IDs
    blue_draft_ids = [str(champ_to_id[champ]) for champ in blue_draft]
    red_draft_ids = [str(champ_to_id[champ]) for champ in red_draft]

    # Blue team perspective
    blue_team_data.append([
        team_to_id[blue_team],
        f"[{', '.join(blue_draft_ids)}]",
        f"[{', '.join(red_draft_ids)}]"
    ])

    # Red team perspective
    red_team_data.append([
        team_to_id[red_team],
        f"[{', '.join(red_draft_ids)}]",
        f"[{', '.join(blue_draft_ids)}]"
    ])

# Write to CSV files
with open('blue_team_drafts.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['team_id', 'ally_draft', 'enemy_draft'])
    writer.writerows(blue_team_data)

with open('red_team_drafts.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['team_id', 'ally_draft', 'enemy_draft'])
    writer.writerows(red_team_data)
