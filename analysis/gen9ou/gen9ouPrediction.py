import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

df = pd.read_csv('analysis/gen9ou/gen9ou.csv')

X = df[['hp', 'atk', 'def', 'spa', 'spd', 'spe', 'physweep', 'spesweep', 'phytank', 'spetank', 'wall', 'total']]
y = df[['rank', 'usage']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=50)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f'Mean Squared Error on Test Set: {mse:.2f}')

hypotheticalHP = 80
hypotheticalAtk = 90
hypotheticalDef = 100
hypotheticalSpa = 110
hypotheticalSpd = 120
hypotheticalSpe = 130

hypotheticalPhySweep = hypotheticalAtk + hypotheticalSpe
hypotheticalSpeSweep = hypotheticalSpa + hypotheticalSpe
hypotheticalPhyTank = hypotheticalAtk + hypotheticalDef
hypotheticalSpeTank = hypotheticalSpa + hypotheticalSpd
hypotheticalWall = hypotheticalHP + hypotheticalDef + hypotheticalSpd
hypotheticalTotal = hypotheticalHP + hypotheticalAtk + hypotheticalDef + hypotheticalSpa + hypotheticalSpd + hypotheticalSpe

hypothetical_pokemon_stats = np.array([hypotheticalHP, hypotheticalAtk, hypotheticalDef, 
                                       hypotheticalSpa, hypotheticalSpd, hypotheticalSpe, 
                                       hypotheticalPhySweep, hypotheticalSpeSweep, hypotheticalPhyTank, 
                                       hypotheticalSpeTank, hypotheticalWall, hypotheticalTotal]).reshape(1,-1)

predicted_ranks = model.predict(hypothetical_pokemon_stats)

print(f'Predicted Rank and Usage Percentage for Hypothetical Pokémon: {predicted_ranks}')