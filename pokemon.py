from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

options = Options()
options.headless = True

gen1dexURL = "https://www.serebii.net/pokemon/gen1pokemon.shtml"
gen2dexURL = "https://www.serebii.net/pokemon/gen2pokemon.shtml"
gen3dexURL = "https://www.serebii.net/pokemon/gen3pokemon.shtml"
gen4dexURL = "https://www.serebii.net/pokemon/gen4pokemon.shtml"
gen5dexURL = "https://www.serebii.net/pokemon/gen5pokemon.shtml"
gen6dexURL = "https://www.serebii.net/pokemon/gen6pokemon.shtml"
gen7dexURL = "https://www.serebii.net/pokemon/gen7pokemon.shtml"
gen8dexURL = "https://www.serebii.net/pokemon/gen8pokemon.shtml"
gen9dexURL = "https://www.serebii.net/pokemon/gen9pokemon.shtml"

pokedex = {

}

URLs = [(151, gen1dexURL), (100, gen2dexURL), (135, gen3dexURL), (107, gen4dexURL), (156, gen5dexURL), (72, gen6dexURL), (88, gen7dexURL), (96, gen8dexURL), (121, gen9dexURL)]

for URL in URLs:
    driver = webdriver.Chrome(options = options)
    driver.get(URL[1])
    time.sleep(5)

    numberOfPokemon = URL[0]
    
    info = driver.find_elements(By.CLASS_NAME, "fooinfo")
    i = 0
    index = 0
    while i < numberOfPokemon:

        pokemon={}
        if (index>=len(info)):
            print(index)
            print(URL[1])
            break
        pokemon["pokedex"]=int(info[index].text[1:])
        index=index+2

        name = info[index].text.lower()
        pokemon["name"]=info[index].text.lower()
        index=index+1

        types = info[index].find_elements(By.TAG_NAME, "a")
        pokemon["type1"]=types[0].get_attribute("href")[37:]
        if (len(types)==1):
            pokemon["type2"]=""
        else:
            pokemon["type2"]=types[1].get_attribute("href")[37:]   
        index=index+1

        abilities = info[index].find_elements(By.TAG_NAME, "a")
        pokemon["ability1"]=abilities[0].text.lower()
        if (len(abilities)==1):
            pokemon["ability2"]=""
            pokemon["ability3"]=""
        elif (len(abilities)==2):
            pokemon["ability2"]=abilities[1].text.lower()
            pokemon["ability3"]=""
        else:
            pokemon["ability2"]=abilities[1].text.lower()
            pokemon["ability3"]=abilities[2].text.lower()
        index=index+1

        pokemon["hp"]=int(info[index].text)
        index=index+1

        pokemon["att"]=int(info[index].text)
        index=index+1

        pokemon["def"]=int(info[index].text)
        index=index+1

        pokemon["spa"]=int(info[index].text)
        index=index+1
        
        pokemon["spd"]=int(info[index].text)
        index=index+1

        pokemon["spe"]=int(info[index].text)
        index=index+1


        
        i=i+1
        pokedex[name]=pokemon




print(json.dumps(pokedex, indent = 4, ensure_ascii = False))

with open("output1.json", "w", encoding = "utf-8") as f:
    json.dump(pokedex, f, ensure_ascii = False, indent = 4)


        