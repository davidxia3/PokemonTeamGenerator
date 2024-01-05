import json

with open('initializationPokedexes/pokedexWithMoves.json', 'r') as file:
    pokedexWithMoves = json.load(file)

pokedexWithStatCombinations = {}
for key, value in pokedexWithMoves.items():
    pokemon = value
    pokemon["physweep"] = pokemon["atk"]+pokemon["spe"]
    pokemon["spesweep"] = pokemon["spa"]+pokemon["spe"]
    pokemon["phytank"] = pokemon["atk"]+pokemon["def"]
    pokemon["spetank"] = pokemon["spa"]+pokemon["spd"]
    pokemon["wall"] = pokemon["hp"]+pokemon["def"]+pokemon["spd"]
    pokemon["total"]=pokemon["hp"]+pokemon["atk"]+pokemon["def"]+pokemon["spa"]+pokemon["spd"]+pokemon["spe"]
    pokedexWithStatCombinations[key] = pokemon

with open("initializationPokedexes/pokedexWithStatCombinations.json", "w", encoding = "utf-8") as f:
    json.dump(pokedexWithStatCombinations,f, ensure_ascii = False, indent = 4)