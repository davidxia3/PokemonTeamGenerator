from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

options = Options()
options.headless = True

with open("pokedex.json", "r") as jsonFile:
    pokedex = json.load(jsonFile)


driver = webdriver.Chrome(options = options) 

for pokemon in pokedex:
    moveList = []
    pokemonURL = "https://www.smogon.com/dex/sv/pokemon/"+pokemon+"/"
    driver.get(pokemonURL)

    moves = driver.find_elements(By.CLASS_NAME, "MoveRow")
    for move in moves:
        moveName = move.find_element(By.CLASS_NAME, "MoveRow-name").text
        moveList.append(moveName)
    pokedex[pokemon]["moves"]=moveList

with open("pokedex.json", "w", encoding = "utf-8") as f:
    json.dump(pokedex,f, ensure_ascii = False, indent = 4)