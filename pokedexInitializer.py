from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

options = Options()
options.headless = True

pokedex ={}

url = 'https://www.smogon.com/dex/sv/pokemon/' 
 
driver = webdriver.Chrome(options = options) 
driver.get(url) 


lastFound = False
first = True
while lastFound==False:
    if first:
        driver.execute_script("window.scrollBy(0,215)")
        first=False
    else:
        driver.execute_script("window.scrollBy(0,630)")

    rows = driver.find_elements(By.CLASS_NAME, "PokemonAltRow")

    for row in rows:
        name = row.find_element(By.CLASS_NAME,  "PokemonAltRow-name").text.lower()
        pokemon={}
        pokemon["name"] = name

        typeList = row.find_element(By.CLASS_NAME, "PokemonAltRow-types")
        types=typeList.text.lower().split("\n",1)
        for i in range(len(types)):
            pokemon["types"+str(i+1)]=types[i]

        abilities = row.find_elements(By.CLASS_NAME, "PokemonAltRow-abilities")
        regularAbilities = abilities[0].text.lower().split("\n",1)
        pokemon["ability2"]=""
        for i in range(len(regularAbilities)):
            pokemon["ability"+str(i+1)]=regularAbilities[i]
        pokemon["hidden ability"]=abilities[1].text.lower()
        

        pokemon["format"]=row.find_element(By.CLASS_NAME, "PokemonAltRow-tags").find_element(By.CLASS_NAME, "FormatList").text.lower() 


        pokemon["hp"] = int(row.find_element(By.CLASS_NAME, "PokemonAltRow-hp").find_element(By.CSS_SELECTOR, "div.PokemonAltRow-hp > span").get_attribute("innerHTML"))

        pokemon["atk"] = int(row.find_element(By.CLASS_NAME, "PokemonAltRow-atk").find_element(By.CSS_SELECTOR, "div.PokemonAltRow-atk > span").get_attribute("innerHTML"))
        
        pokemon["def"] = int(row.find_element(By.CLASS_NAME, "PokemonAltRow-def").find_element(By.CSS_SELECTOR, "div.PokemonAltRow-def > span").get_attribute("innerHTML"))

        pokemon["spa"] = int(row.find_element(By.CLASS_NAME, "PokemonAltRow-spa").find_element(By.CSS_SELECTOR, "div.PokemonAltRow-spa > span").get_attribute("innerHTML"))

        pokemon["spd"] = int(row.find_element(By.CLASS_NAME, "PokemonAltRow-spd").find_element(By.CSS_SELECTOR, "div.PokemonAltRow-spd > span").get_attribute("innerHTML"))

        pokemon["spe"] = int(row.find_element(By.CLASS_NAME, "PokemonAltRow-spe").find_element(By.CSS_SELECTOR, "div.PokemonAltRow-spe > span").get_attribute("innerHTML"))

        pokedex[name]=pokemon
        if name == "zygarde-complete":
            lastFound=True



with open("pokedex.json", "w", encoding = "utf-8") as f:
    json.dump(pokedex,f, ensure_ascii = False, indent = 4)

