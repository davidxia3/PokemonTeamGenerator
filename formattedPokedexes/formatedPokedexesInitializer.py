import json

dex_mapping = {
    "national dex": "natDex",
    "ag": "agDex",
    "uber": "uberDex",
    "ou": "ouDex",
    "uu": "uuDex",
    "ru": "ruDex",
    "nu": "nuDex",
    "pu": "puDex",
    "zu": "zuDex",
    "lc": "lcDex",
    "nfe": "nfeDex",
    "cap": "capDex"
}

with open('pokedexWithStatCombinations.json', 'r') as file:
    pokedex = json.load(file)

dex_data = {key: {} for key in dex_mapping.values()}

for key, value in pokedex.items():
    pokemon = value
    format_key = value["format"].lower()
    
    if format_key in dex_mapping:
        dex_key = dex_mapping[format_key]
        dex_data[dex_key][key] = pokemon

for dex_key, dex_dict in dex_data.items():
    with open(f"{dex_key}.json", "w", encoding="utf-8") as f:
        json.dump(dex_dict, f, ensure_ascii=False, indent=4)