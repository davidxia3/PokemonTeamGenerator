import json

with open("data/gen9ou/gen9ou-1825.txt", 'r') as file:
    rows = file.readlines()

totalBattles = int(rows[0].strip()[15:])
aveWeightPerTeam = float(rows[1].strip()[18:])

pokedex={}

for i in range(5, len(rows)-1):
    pokemon={}
    columns = [col.strip() for col in rows[i].split('|') if col.strip()]
    rank = int(columns[0].strip())
    name = columns[1].strip().lower()
    usagePercent = float(columns[2].strip('%'))

    pokemon["name"]=name
    pokemon["rank"]=rank
    pokemon["usagePercent"]=usagePercent
    pokedex[name]=pokemon

with open("data/gen9ou/gen9ou.json", 'w') as json_file:
        json.dump(pokedex, json_file, indent=4)
