import json
import random

with open('pokedexWithStatCombinations.json', 'r') as file:
    pokedex = json.load(file)

randomTeam = random.sample(list(pokedex.keys()), k=6)

for pokemon in randomTeam:
    print(pokemon)
    print(json.dumps(pokedex[pokemon], indent = 4))