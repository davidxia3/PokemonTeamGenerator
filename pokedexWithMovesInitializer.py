from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

options = Options()
options.headless = True

with open('pokedex.json', 'r') as file:
    pokedex = json.load(file)

pokedexWithMoves={}

print(pokedex)

for key, value in pokedex.items():
    pokemon={}
    pokemon["name"]=key


    
    pokedexWithMoves[key]=pokemon

with open("pokedexWithMoves.json", "w", encoding = "utf-8") as f:
    json.dump(pokedexWithMoves,f, ensure_ascii = False, indent = 4)