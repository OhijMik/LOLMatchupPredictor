import csv
import pandas as pd

# Team name to ID mapping
team_meta = pd.read_csv("data/team_meta.csv")
team_to_id = dict(zip(team_meta["name"], team_meta["team_id"]))

# Champion name to ID mapping
champion_name_meta = pd.read_csv("data/champion_meta.csv")
champ_to_id = dict(zip(champion_name_meta["name"], champion_name_meta["champion_id"]))

# Input data with winner column
input_data = """DRX	OKSavingsBank BRION	OKSavingsBank BRION	Jax,Wukong,Aurora,Kai'Sa,Poppy	Yorick,Trundle,Ryze,Jhin,Maokai
OKSavingsBank BRION	DRX	DRX	Rumble,Vi,Ahri,Zeri,Nautilus	Galio,Xin Zhao,Azir,Sivir,Leona
DRX	OKSavingsBank BRION	OKSavingsBank BRION	Gwen,Pantheon,Annie,Lucian,Braum	Ambessa,Jarvan IV,Orianna,Corki,Rakan
Nongshim RedForce	KT Rolster	KT Rolster	Gwen,Nocturne,Orianna,Sivir,Maokai	Ambessa,Xin Zhao,Annie,Kai'Sa,Rakan
Nongshim RedForce	KT Rolster	KT Rolster	Aurora,Wukong,Galio,Jhin,Poppy	Rumble,Jarvan IV,Ryze,Ezreal,Alistar
Dplus KIA	DN Freecs	Dplus KIA	Renekton,Vi,Ahri,Lucian,Braum	K'Sante,Kindred,Ryze,Corki,Rell
DN Freecs	Dplus KIA	DN Freecs	Aatrox,Lee Sin,Galio,Yunara,Alistar	Ambessa,Xin Zhao,Annie,Jhin,Bard
DN Freecs	Dplus KIA	Dplus KIA	Rumble,Wukong,Taliyah,Sivir,Karma	Ornn,Jarvan IV,Orianna,Kai'Sa,Neeko
T1	Gen.G	Gen.G	Yorick,Skarner,Viktor,Yunara,Tahm Kench	K'Sante,Wukong,Annie,Jhin,Rakan
Gen.G	T1	Gen.G	Gwen,Pantheon,Galio,Zeri,Rell	Rumble,Trundle,Ryze,Sivir,Renata Glasc
T1	Gen.G	T1	Renekton,Xin Zhao,Orianna,Corki,Poppy	Sion,Vi,Aurora,Kai'Sa,Neeko
Nongshim RedForce	Hanwha Life Esports	Hanwha Life Esports	Aatrox,Vi,Akali,Varus,Elise	Ambessa,Sejuani,Taliyah,Sivir,Leona
Hanwha Life Esports	Nongshim RedForce	Hanwha Life Esports	Rumble,Wukong,Aurora,Corki,Rakan	Gwen,Xin Zhao,Orianna,Jhin,Maokai
DRX	BNK FEARX	BNK FEARX	K'Sante,Lee Sin,Azir,Jhin,Alistar	Sion,Sylas,Yone,Kalista,Renata Glasc
BNK FEARX	DRX	BNK FEARX	Jax,Pantheon,Akali,Xayah,Rakan	Ambessa,Jarvan IV,Taliyah,Lucian,Braum
BNK FEARX	DRX	DRX	Rumble,Wukong,Ryze,Sivir,Neeko	Gwen,Xin Zhao,Orianna,Corki,Bard
KT Rolster	Gen.G	Gen.G	K'Sante,Jarvan IV,Ahri,Yunara,Alistar	Sion,Xin Zhao,Taliyah,Corki,Rakan
Gen.G	KT Rolster	Gen.G	Aurora,Wukong,Orianna,Jhin,Pyke	Rumble,Trundle,Ryze,Ezreal,Bard
OKSavingsBank BRION	Dplus KIA	Dplus KIA	Yorick,Wukong,Taliyah,Zeri,Rakan	Rumble,Trundle,Ahri,Jhin,Nautilus
Dplus KIA	OKSavingsBank BRION	Dplus KIA	Aurora,Jarvan IV,Annie,Corki,Bard	Ambessa,Pantheon,Orianna,Sivir,Rell
DN Freecs	BNK FEARX	BNK FEARX	K'Sante,Nocturne,Orianna,Zeri,Alistar	Sion,Jarvan IV,Ryze,Sivir,Rakan
DN Freecs	BNK FEARX	BNK FEARX	Ambessa,Wukong,Aurora,Corki,Neeko	Renekton,Xin Zhao,Annie,Yunara,Lulu
T1	Hanwha Life Esports	T1	Renekton,Nocturne,Orianna,Lucian,Bard	Ornn,Jarvan IV,Akali,Jhin,Rell
Hanwha Life Esports	T1	Hanwha Life Esports	Gwen,Xin Zhao,Taliyah,Ezreal,Alistar	Jax,Skarner,Ryze,Corki,Rakan
T1	Hanwha Life Esports	T1	Rumble,Wukong,Galio,Sivir,Poppy	Ambessa,Vi,Annie,Varus,Nautilus
T1	KT Rolster	KT Rolster	Gwen,Pantheon,Galio,Lucian,Braum	Ambessa,Wukong,Annie,Ziggs,Nautilus
KT Rolster	T1	KT Rolster	Rumble,Trundle,Taliyah,Corki,Leona	Aurora,Xin Zhao,Orianna,Jhin,Rakan
BNK FEARX	Dplus KIA	Dplus KIA	K'Sante,Nocturne,Taliyah,Kai'Sa,Neeko	Sion,Jarvan IV,Ahri,Zeri,Lulu
BNK FEARX	Dplus KIA	Dplus KIA	Rumble,Pantheon,Galio,Varus,Alistar	Gwen,Xin Zhao,Annie,Jhin,Rakan
DN Freecs	OKSavingsBank BRION	DN Freecs	K'Sante,Lee Sin,Orianna,Kai'Sa,Alistar	Sion,Zed,Annie,Sivir,Neeko
OKSavingsBank BRION	DN Freecs	OKSavingsBank BRION	Yorick,Maokai,Yone,Varus,Braum	Ambessa,Jarvan IV,Taliyah,Lucian,Rell
OKSavingsBank BRION	DN Freecs	DN Freecs	Aurora,Poppy,Azir,Jhin,Bard	Rumble,Vi,Ziggs,Corki,Rakan
Gen.G	Hanwha Life Esports	Gen.G	Renekton,Xin Zhao,Ryze,Tristana,Blitzcrank	Gragas,Trundle,Cassiopeia,Kai'Sa,Alistar
Hanwha Life Esports	Gen.G	Hanwha Life Esports	Ambessa,Poppy,Azir,Lucian,Braum	Yorick,Pantheon,Ziggs,Jhin,Rakan
Hanwha Life Esports	Gen.G	Gen.G	Gwen,Vi,Taliyah,Yunara,Rell	Rumble,Wukong,Orianna,Corki,Neeko
DRX	Dplus KIA	Dplus KIA	K'Sante,Viego,Taliyah,Sivir,Nautilus	Yorick,Trundle,Ahri,Jinx,Tahm Kench
Dplus KIA	DRX	Dplus KIA	Aurora,Jarvan IV,Cassiopeia,Jhin,Bard	Gwen,Xin Zhao,Ryze,Ezreal,Alistar
Dplus KIA	DRX	DRX	Ornn,Wukong,Orianna,Corki,Leona	Rumble,Pantheon,Annie,Kai'Sa,Rell
T1	Nongshim RedForce	T1	Jax,Zed,Ryze,Lucian,Braum	Yorick,Trundle,Annie,Jinx,Milio
Nongshim RedForce	T1	Nongshim RedForce	Ambessa,Pantheon,Taliyah,Ziggs,Leona	Aurora,Jarvan IV,Ahri,Varus,Bard
Nongshim RedForce	T1	T1	Ornn,Wukong,Orianna,Sivir,Alistar	Rumble,Xin Zhao,Galio,Jhin,Poppy
BNK FEARX	OKSavingsBank BRION	BNK FEARX	K'Sante,Jarvan IV,Azir,Kalista,Renata Glasc	Yorick,Pantheon,LeBlanc,Lucian,Braum
OKSavingsBank BRION	BNK FEARX	OKSavingsBank BRION	Sion,Trundle,Orianna,Corki,Neeko	Renekton,Vi,Viktor,Jhin,Alistar
OKSavingsBank BRION	BNK FEARX	BNK FEARX	Gwen,Wukong,Ahri,Sivir,Rell	Rumble,Xin Zhao,Taliyah,Kai'Sa,Rakan
KT Rolster	Hanwha Life Esports	Hanwha Life Esports	Sion,Trundle,Ahri,Aphelios,Lulu	Aatrox,Ivern,Taliyah,Kai'Sa,Neeko
Hanwha Life Esports	KT Rolster	Hanwha Life Esports	Ambessa,Jarvan IV,Aurora,Zeri,Alistar	Renekton,Xin Zhao,Orianna,Sivir,Braum
KT Rolster	Hanwha Life Esports	KT Rolster	Gwen,Pantheon,Ryze,Corki,Nautilus	Rumble,Wukong,Galio,Jhin,Bard
Nongshim RedForce	Gen.G	Gen.G	Ambessa,Poppy,Ryze,Ezreal,Elise	Renekton,Vi,Galio,Caitlyn,Neeko
Gen.G	Nongshim RedForce	Gen.G	Gwen,Skarner,Azir,Corki,Bard	Aurora,Wukong,Taliyah,Jhin,Alistar
DN Freecs	DRX	DRX	Sion,Wukong,Taliyah,Kai'Sa,Rell	Ambessa,Pantheon,Ryze,Sivir,Leona
DRX	DN Freecs	DRX	Aurora,Xin Zhao,Galio,Lucian,Braum	Rumble,Nocturne,Orianna,Jhin,Alistar
Dplus KIA	OKSavingsBank BRION	OKSavingsBank BRION	Ambessa,Vi,Ahri,Ezreal,Karma	Renekton,Maokai,Yone,Lucian,Nautilus
OKSavingsBank BRION	Dplus KIA	OKSavingsBank BRION	Rumble,Wukong,Annie,Corki,Rell	Ornn,Trundle,Orianna,Sivir,Bard
Gen.G	Hanwha Life Esports	Gen.G	Sion,Pantheon,Ziggs,Lucian,Braum	Aatrox,Jarvan IV,Galio,Sivir,Karma
Hanwha Life Esports	Gen.G	Hanwha Life Esports	Ambessa,Vi,Aurora,Xayah,Leona	Yorick,Xin Zhao,Ryze,Ezreal,Rell
Hanwha Life Esports	Gen.G	Gen.G	Rumble,Poppy,Ahri,Yunara,Alistar	Gwen,Wukong,Azir,Corki,Rakan
DRX	BNK FEARX	DRX	Ambessa,Sejuani,Ryze,Sivir,Bard	Sion,Vi,Cassiopeia,Zeri,Karma
BNK FEARX	DRX	BNK FEARX	Rumble,Jarvan IV,Taliyah,Jhin,Rell	Aatrox,Trundle,Ahri,Corki,Neeko
DRX	BNK FEARX	DRX	Aurora,Wukong,Annie,Xayah,Rakan	Gwen,Xin Zhao,Galio,Lucian,Braum
KT Rolster	Nongshim RedForce	KT Rolster	Sion,Jarvan IV,Azir,Ezreal,Neeko	Camille,Trundle,Taliyah,Corki,Bard
Nongshim RedForce	KT Rolster	Nongshim RedForce	Ambessa,Viego,Galio,Varus,Elise	Renekton,Skarner,Annie,Jhin,Poppy
Nongshim RedForce	KT Rolster	KT Rolster	Rumble,Wukong,Orianna,Aphelios,Nautilus	Ornn,Xin Zhao,Ryze,Sivir,Alistar
Hanwha Life Esports	T1	T1	Rumble,Maokai,Yone,Corki,Blitzcrank	Yorick,Trundle,Annie,Lucian,Braum
Hanwha Life Esports	T1	T1	Jax,Xin Zhao,Galio,Varus,Rell	Ambessa,Wukong,Orianna,Sivir,Bard
OKSavingsBank BRION	DN Freecs	DN Freecs	Ambessa,Skarner,Viktor,Jhin,Karma	K'Sante,Hecarim,Ryze,Kai'Sa,Neeko
DN Freecs	OKSavingsBank BRION	DN Freecs	Rumble,Wukong,Annie,Lucian,Braum	Gwen,Vi,Aurora,Corki,Alistar
OKSavingsBank BRION	DN Freecs	OKSavingsBank BRION	Renekton,Maokai,Yone,Yunara,Nautilus	Sion,Trundle,Azir,Varus,Rell
DRX	Dplus KIA	Dplus KIA	Rumble,Pantheon,Viktor,Miss Fortune,Nautilus	Ornn,Wukong,Annie,Jhin,Rell
Dplus KIA	DRX	Dplus KIA	Aurora,Trundle,Orianna,Corki,Neeko	Gwen,Xin Zhao,Ryze,Sivir,Karma
Nongshim RedForce	Gen.G	Gen.G	Rumble,Skarner,Azir,Sivir,Nautilus	Yorick,Pantheon,Aurora,Kai'Sa,Rakan
Gen.G	Nongshim RedForce	Gen.G	Gwen,Wukong,Annie,Corki,Neeko	Ambessa,Xin Zhao,Orianna,Jhin,Alistar
BNK FEARX	DN Freecs	BNK FEARX	Sion,Lee Sin,Azir,Jhin,Alistar	K'Sante,Trundle,Taliyah,Aphelios,Nautilus
DN Freecs	BNK FEARX	DN Freecs	Rumble,Pantheon,Aurora,Sivir,Rell	Aatrox,Nocturne,Ryze,Kai'Sa,Rakan
BNK FEARX	DN Freecs	BNK FEARX	Gwen,Wukong,Annie,Zeri,Lulu	Ambessa,Xin Zhao,Galio,Lucian,Nami
KT Rolster	T1	T1	Rumble,Trundle,Taliyah,Corki,Rell	Gwen,Wukong,Annie,Jhin,Blitzcrank
T1	KT Rolster	T1	Ambessa,Jarvan IV,Orianna,Varus,Bard	Sion,Xin Zhao,Ryze,Sivir,Neeko
DN Freecs	Dplus KIA	Dplus KIA	Ambessa,Jarvan IV,Galio,Xayah,Rakan	Aurora,Trundle,Jayce,Corki,Janna
DN Freecs	Dplus KIA	Dplus KIA	Rumble,Vi,Ahri,Lucian,Braum	Gwen,Wukong,Taliyah,Sivir,Neeko
KT Rolster	Gen.G	Gen.G	Ornn,Xin Zhao,Annie,Xayah,Rakan	Rumble,Skarner,Galio,Ezreal,Poppy
KT Rolster	Gen.G	Gen.G	Ambessa,Trundle,Ryze,Jhin,Rell	Gwen,Vi,Taliyah,Corki,Neeko
Nongshim RedForce	T1	T1	Gwen,Wukong,Corki,Kalista,Renata Glasc	Ambessa,Xin Zhao,Galio,Sivir,Poppy
Nongshim RedForce	T1	T1	Rumble,Trundle,Ryze,Xayah,Lulu	Aurora,Nocturne,Orianna,Jhin,Alistar
DRX	OKSavingsBank BRION	OKSavingsBank BRION	Cho'Gath,Viego,Ryze,Aphelios,Thresh	Sion,Zed,Viktor,Sivir,Blitzcrank
OKSavingsBank BRION	DRX	OKSavingsBank BRION	Rumble,Wukong,Annie,Corki,Nautilus	Ambessa,Jarvan IV,Orianna,Jhin,Alistar
DRX	OKSavingsBank BRION	DRX	Gwen,Xin Zhao,Galio,Yunara,Rakan	Aurora,Vi,Cassiopeia,Kai'Sa,Rell
KT Rolster	Hanwha Life Esports	Hanwha Life Esports	Sion,Trundle,Viktor,Jhin,Karma	Aatrox,Jarvan IV,Orianna,Kai'Sa,Neeko
KT Rolster	Hanwha Life Esports	Hanwha Life Esports	Rumble,Xin Zhao,Taliyah,Aphelios,Nautilus	Ornn,Wukong,Ryze,Yunara,Alistar
Dplus KIA	BNK FEARX	BNK FEARX	Ambessa,Lee Sin,Ryze,Yunara,Neeko	Renekton,Trundle,Ahri,Kai'Sa,Rell
BNK FEARX	Dplus KIA	BNK FEARX	Gwen,Xin Zhao,Azir,Lucian,Braum	Rumble,Sejuani,Yone,Varus,Alistar
T1	Gen.G	Gen.G	Jax,Nocturne,Sylas,Xayah,Neeko	Yorick,Vi,Corki,Ziggs,Nautilus
Gen.G	T1	Gen.G	Ambessa,Xin Zhao,Galio,Yunara,Rakan	Rumble,Jarvan IV,Orianna,Lucian,Nami
Gen.G	T1	T1	Gwen,Wukong,Annie,Sivir,Rell	Aurora,Trundle,Ryze,Jhin,Bard
DN Freecs	DRX	DN Freecs	Gragas,Jarvan IV,Galio,Kai'Sa,Neeko	Renekton,Nocturne,Sylas,Sivir,Lulu
DRX	DN Freecs	DRX	Aatrox,Xin Zhao,Taliyah,Jhin,Alistar	Sion,Skarner,Azir,Senna,Bard
DRX	DN Freecs	DN Freecs	Gwen,Wukong,Aurora,Xayah,Nautilus	Rumble,Vi,Annie,Yunara,Rell
OKSavingsBank BRION	BNK FEARX	BNK FEARX	Jax,Maokai,Yone,Varus,Neeko	Ambessa,Xin Zhao,Orianna,Jhin,Bard
OKSavingsBank BRION	BNK FEARX	BNK FEARX	Ornn,Trundle,Azir,Lucian,Braum	Rumble,Wukong,Taliyah,Yunara,Rakan
Nongshim RedForce	Hanwha Life Esports	Hanwha Life Esports	Jayce,Nocturne,Ryze,Sivir,Shen	K'Sante,Jarvan IV,Taliyah,Kai'Sa,Neeko
Hanwha Life Esports	Nongshim RedForce	Hanwha Life Esports	Rumble,Wukong,Orianna,Xayah,Rakan	Gwen,Xin Zhao,Annie,Yunara,Lulu
Nongshim RedForce	Gen.G	Gen.G	Ambessa,Skarner,Azir,Zeri,Shen	Yorick,Pantheon,Aurora,Sivir,Rell
Nongshim RedForce	Gen.G	Gen.G	Rumble,Wukong,Galio,Ezreal,Leona	Gwen,Xin Zhao,Annie,Corki,Neeko
DN Freecs	OKSavingsBank BRION	OKSavingsBank BRION	Sion,Xin Zhao,Azir,Senna,Nautilus	Cho'Gath,Maokai,Yone,Kai'Sa,Neeko
DN Freecs	OKSavingsBank BRION	OKSavingsBank BRION	Rumble,Trundle,Ryze,Corki,Rell	Aurora,Wukong,Cassiopeia,Varus,Poppy
BNK FEARX	DRX	DRX	Gwen,Naafiri,Galio,Sivir,Leona	Ambessa,Jarvan IV,Aurora,Zeri,Lulu
DRX	BNK FEARX	DRX	Renekton,Xin Zhao,Viktor,Senna,Nautilus	K'Sante,Vi,Ryze,Corki,Neeko
BNK FEARX	DRX	BNK FEARX	Aatrox,Nocturne,Orianna,Varus,Rell	Rumble,Trundle,Ahri,Jhin,Alistar
Hanwha Life Esports	T1	T1	Aatrox,Maokai,Azir,Senna,Alistar	K'Sante,Trundle,Taliyah,Sivir,Neeko
T1	Hanwha Life Esports	T1	Gwen,Jarvan IV,Galio,Jhin,Bard	Ambessa,Wukong,Orianna,Lucian,Rakan
DN Freecs	Dplus KIA	Dplus KIA	Rumble,Trundle,Viktor,Lucian,Braum	Aurora,Zed,Ryze,Senna,Galio
Dplus KIA	DN Freecs	Dplus KIA	Sion,Vi,Taliyah,Varus,Karma	Cho'Gath,Poppy,Azir,Sivir,Rell
KT Rolster	Gen.G	Gen.G	Yorick,Trundle,Taliyah,Ziggs,Leona	Ambessa,Vi,Ryze,Senna,Bard
Gen.G	KT Rolster	Gen.G	Gwen,Wukong,Galio,Kai'Sa,Rell	Aurora,Xin Zhao,Annie,Sivir,Nautilus
Nongshim RedForce	Hanwha Life Esports	Hanwha Life Esports	Sylas,Trundle,Azir,Sivir,Leona	Rumble,Sejuani,Yone,Kai'Sa,Bard
Nongshim RedForce	Hanwha Life Esports	Hanwha Life Esports	Gwen,Xin Zhao,Ryze,Corki,Rell	Aurora,Wukong,Orianna,Lucian,Braum
OKSavingsBank BRION	BNK FEARX	BNK FEARX	Ornn,Xin Zhao,Akali,Corki,Poppy	Renekton,Nocturne,Orianna,Kai'Sa,Alistar
BNK FEARX	OKSavingsBank BRION	BNK FEARX	Rumble,Wukong,Azir,Sivir,Braum	Gwen,Vi,Ahri,Lucian,Rell
KT Rolster	T1	T1	Jax,Skarner,Viktor,Varus,Poppy	Gwen,Nocturne,Galio,Xayah,Rakan
KT Rolster	T1	T1	Rumble,Wukong,Cassiopeia,Corki,Nautilus	Ornn,Xin Zhao,Ryze,Sivir,Neeko
DRX	Dplus KIA	Dplus KIA	Sion,Jarvan IV,Cassiopeia,Varus,Alistar	Cho'Gath,Viego,Sylas,Jhin,Nautilus
Dplus KIA	DRX	Dplus KIA	Ambessa,Skarner,Azir,Sivir,Karma	Rumble,Sejuani,Yone,Corki,Neeko
DRX	Dplus KIA	DRX	Gwen,Wukong,Taliyah,Miss Fortune,Rell	Aurora,Xin Zhao,Twisted Fate,Ezreal,Braum
Nongshim RedForce	T1	T1	K'Sante,Viego,Galio,Senna,Tahm Kench	Ambessa,Nocturne,Orianna,Jhin,Bard
T1	Nongshim RedForce	T1	Gwen,Jarvan IV,Ryze,Varus,Poppy	Rumble,Wukong,Ahri,Sivir,Nautilus
DRX	DN Freecs	DRX	K'Sante,Viego,Ryze,Ezreal,Neeko	Aatrox,Skarner,Cassiopeia,Corki,Bard
DN Freecs	DRX	DN Freecs	Sion,Trundle,Azir,Sivir,Rell	Ambessa,Vi,Aurora,Kai'Sa,Rakan
DN Freecs	DRX	DRX	Rumble,Nocturne,Orianna,Zeri,Lulu	Ornn,Xin Zhao,Taliyah,Lucian,Nautilus
KT Rolster	Hanwha Life Esports	Hanwha Life Esports	Jayce,Jarvan IV,Taliyah,Sivir,Alistar	K'Sante,Xin Zhao,Azir,Corki,Rakan
Hanwha Life Esports	KT Rolster	Hanwha Life Esports	Rumble,Wukong,Annie,Varus,Poppy	Gwen,Trundle,Malzahar,Jhin,Rell
BNK FEARX	Dplus KIA	Dplus KIA	Gwen,Xin Zhao,Ahri,Varus,Rakan	Rumble,Wukong,Orianna,Jhin,Maokai
Dplus KIA	BNK FEARX	Dplus KIA	Jayce,Trundle,Twisted Fate,Senna,Alistar	Ambessa,Jarvan IV,Taliyah,Lucian,Braum
DRX	OKSavingsBank BRION	OKSavingsBank BRION	K'Sante,Jarvan IV,Ryze,Sivir,Rakan	Renekton,Nidalee,Cassiopeia,Kai'Sa,Rell
OKSavingsBank BRION	DRX	OKSavingsBank BRION	Aatrox,Vi,Ahri,Ezreal,Braum	Rumble,Trundle,Azir,Lucian,Leona
OKSavingsBank BRION	DRX	DRX	Sion,Xin Zhao,Annie,Corki,Alistar	Ambessa,Wukong,Aurora,Miss Fortune,Poppy
Gen.G	T1	T1	Renekton,Trundle,Viktor,Senna,Alistar	Gragas,Xin Zhao,Ryze,Aphelios,Thresh
T1	Gen.G	T1	Jayce,Sejuani,Azir,Xayah,Rakan	K'Sante,Skarner,Twisted Fate,Lucian,Braum
T1	Gen.G	Gen.G	Rumble,Vi,Annie,Corki,Neeko	Gwen,Wukong,Orianna,Jhin,Bard
Nongshim RedForce	KT Rolster	KT Rolster	Camille,Sejuani,Yone,Varus,Shen	Yorick,Zed,Aurora,Ziggs,Alistar
KT Rolster	Nongshim RedForce	KT Rolster	Gwen,Wukong,Taliyah,Corki,Rakan	Rumble,Xin Zhao,Azir,Senna,Leona
DN Freecs	BNK FEARX	BNK FEARX	Aatrox,Trundle,Aurora,Jinx,Nautilus	Yorick,Wukong,Annie,Sivir,Rell
DN Freecs	BNK FEARX	BNK FEARX	Gwen,Nocturne,Orianna,Zeri,Lulu	Rumble,Vi,Taliyah,Kai'Sa,Alistar
Hanwha Life Esports	Gen.G	Gen.G	Ambessa,Sejuani,Taliyah,Lucian,Braum	K'Sante,Jarvan IV,Azir,Corki,Rell
Gen.G	Hanwha Life Esports	Gen.G	Aurora,Wukong,Annie,Senna,Alistar	Gwen,Xin Zhao,Ryze,Jhin,Neeko
Dplus KIA	OKSavingsBank BRION	OKSavingsBank BRION	Ambessa,Lee Sin,Ryze,Miss Fortune,Nautilus	Rumble,Trundle,Cassiopeia,Lucian,Alistar
OKSavingsBank BRION	Dplus KIA	OKSavingsBank BRION	Cho'Gath,Xin Zhao,Annie,Corki,Rell	Sion,Zed,Syndra,Senna,Braum
Dplus KIA	OKSavingsBank BRION	Dplus KIA	Gwen,Poppy,Taliyah,Sivir,Karma	Aurora,Wukong,Ahri,Ezreal,Neeko"""

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
