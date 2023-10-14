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

    generations = driver.find_element(By.CLASS_NAME, "OtherGensList").find_elements(By.TAG_NAME, "a")
    generationList=[]
    for gen in generations:
        generationList.append(gen.get_attribute("href"))
    generationList.append(pokemonURL)
    
    for generation in generationList:
        driver.get(generation)

        moves = driver.find_elements(By.CLASS_NAME, "MoveRow")
        for move in moves:
            moveName = move.find_element(By.CLASS_NAME, "MoveRow-name").text
            if moveName not in moveList:
                moveList.append(moveName)
    pokedex[pokemon]["moves"]=moveList

with open("pokedex.json", "w", encoding = "utf-8") as f:
    json.dump(pokedex,f, ensure_ascii = False, indent = 4)