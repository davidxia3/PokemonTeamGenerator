import pandas as pd
import json

with open('initializationPokedexes/pokedexWithStatCombinations.json', 'r') as json_file:
    data = json.load(json_file)

with open("data/gen9ag/gen9ag.json", 'r') as json_file:
    agDex = json.load(json_file)

ouPokemon = list(agDex.keys())

df = pd.DataFrame(list(data.values()))

columns_to_keep = ['name','hp', 'atk', 'def','spa','spd','spe','physweep','spesweep','phytank','spetank','wall','total']
df = df[columns_to_keep]


df = df[df['name'].isin(ouPokemon)]


df['rank'] = df['name'].map(lambda x: agDex.get(x, {}).get('rank'))
df['usage'] = df['name'].map(lambda x: agDex.get(x, {}).get('usagePercent'))


df.to_csv('analysis/gen9ag/gen9ag.csv', index=False)