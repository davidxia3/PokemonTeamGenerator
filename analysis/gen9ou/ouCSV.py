import pandas as pd
import json

with open('initializationPokedexes/pokedexWithStatCombinations.json', 'r') as json_file:
    data = json.load(json_file)

with open("data/gen9ou/gen9ou.json", 'r') as json_file:
    ouDex = json.load(json_file)

ouPokemon = list(ouDex.keys())

df = pd.DataFrame(list(data.values()))

columns_to_keep = ['name','hp', 'atk', 'def','spa','spd','spe','physweep','spesweep','phytank','spetank','wall','total']
df = df[columns_to_keep]


df = df[df['name'].isin(ouPokemon)]


df['rank'] = df['name'].map(lambda x: ouDex.get(x, {}).get('rank'))
df['usage'] = df['name'].map(lambda x: ouDex.get(x, {}).get('usagePercent'))


df.to_csv('analysis/gen9ou/gen9ou.csv', index=False)