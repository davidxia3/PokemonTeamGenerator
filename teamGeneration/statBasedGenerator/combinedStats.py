import json

dexes = ["natDex", "agDex", "uberDex", "ouDex", "uuDex", "ruDex", "nuDex", "puDex", "zuDex", "lcDex", "nfeDex", "capDex"]

bestTeams = {}

for dex in dexes:
    with open('formattedPokedexes/' + dex + '.json', 'r') as file:
        pokedex = json.load(file)

    format = {}

    selected_pokemon = set()

    categories = ["physweep", "spesweep", "phytank", "spetank", "wall", "total"]

    for category in categories:
        greatest_value = 0
        greatest_pokemon = {}
        greatest_pokemon_name = ""

        for key, value in pokedex.items():
            if key not in selected_pokemon:
                if value[category] > greatest_value:
                    greatest_value = value[category]
                    greatest_pokemon = value
                    greatest_pokemon_name = key

        selected_pokemon.add(greatest_pokemon_name)

        if greatest_pokemon_name!="":
            format[greatest_pokemon_name] = greatest_pokemon

    bestTeams[dex] = format

with open("teamGeneration/statBasedGenerator/bestCombinedStats.json", "w", encoding="utf-8") as f:
    json.dump(bestTeams, f, ensure_ascii=False, indent=4)
