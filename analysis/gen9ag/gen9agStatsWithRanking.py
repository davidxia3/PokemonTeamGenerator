import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import json

with open('data/gen9ag/gen9ag.json', 'r') as file:
    agRankings = json.load(file)

with open('initializationPokedexes/pokedexWithStatCombinations.json', 'r') as file:
    dex = json.load(file)

ranks=[]

stats = ["hp","atk","def","spa","spd","spe","physweep","spesweep","phytank","spetank","wall","total"]

model = LinearRegression()

first = True
for stat in stats:
    data = []
    for key,value in agRankings.items():
        try:
            data.append(dex[key][stat])
            if first:
                ranks.append(value["rank"])   
        except:
            pass
    first=False
    dataArray = np.array(data).reshape(-1,1)

    model.fit(dataArray, ranks)
    predictions = model.predict(dataArray)
    plt.scatter(dataArray, ranks, color='blue', label='Actual data', s=5)
    plt.plot(dataArray, predictions, color='red', linewidth=2, label='Linear regression line')
    plt.xlabel(stat)
    plt.ylabel('Ranks')
    plt.title(f'{stat} - R-squared: {model.score(dataArray, ranks):.4f}')
    plt.legend()
    plt.ylim(0, 744)
    plt.show()