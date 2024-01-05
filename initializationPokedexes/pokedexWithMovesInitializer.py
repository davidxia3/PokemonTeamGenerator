from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

options = Options()
options.headless = True

with open('initializationPokedexes/pokedex.json', 'r') as file:
    pokedex = json.load(file)

pokedexWithMoves={}

for key, value in pokedex.items():
    pokemon=value
    url = "https://www.smogon.com/dex/sv/pokemon/"+ key
    driver = webdriver.Chrome(options = options) 
    driver.get(url)     
    print(key)
    driver.implicitly_wait(0.5)

    exportButtons = driver.find_elements(By.CLASS_NAME, "ExportButton")
    for exportButton in exportButtons:
        exportButton.click()
        reactid = exportButton.get_attribute("data-reactid")
        
        strategyNameReactid = reactid[:-1]+'1'
        strategyName = driver.find_element(By.CSS_SELECTOR, f'[data-reactid="{strategyNameReactid}"]').text
        strategyTextReactid = reactid[:-1]+'2.0.1'
        strategyText = driver.find_element(By.CSS_SELECTOR, f'[data-reactid="{strategyTextReactid}"]').text
        pokemon["strategy: "+strategyName]=strategyText

    if len(exportButtons)==0:
        pokemon["strategy"]="No Strategies"

    moveRows = driver.find_elements(By.CLASS_NAME, "MoveRow  ")
    moves=""
    for moveRow in moveRows:
        moveLink = moveRow.find_element(By.CLASS_NAME, "MoveLink")
        moveLinkText = moveLink.get_attribute("href")
        moveLinkTextParts = moveLinkText.split('/')
        moveName = moveLinkTextParts[-2]
        moves=moves+moveName+", "

    pokemon["moves"]=moves
    
    pokedexWithMoves[key]=pokemon

with open("initializationPokedexes/pokedexWithMoves.json", "w", encoding = "utf-8") as f:
    json.dump(pokedexWithMoves,f, ensure_ascii = False, indent = 4)