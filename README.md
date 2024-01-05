initializationPokedexes:
  Uses Selenium to scrape the Smogon webpage for all Pokemon ('https://www.smogon.com/dex/sv/pokemon/') as well as each 
  individual Pokemon's Smogon site for data including, name, types, abilities, hidden ability, format, hitpoint stat, 
  attack stat, defense stat, special attack stat, special defense stat, speed stat, competitive strategies, 
  all known moves, physical sweep stat (attack+speed), special sweep stat (special attack+speed), physical tank stat 
  (attack+defense), special tank stat (special attack+special defense), wall stat (hp + defense + special defense).
data:
  Includes downloaded txt files from Smogon's competitive stats webpage. Filters and cleans the data into a json file 
  that includes the ranks and usage percentage stats for each Pokemon from both the OU (overused) and AG (anything goes) 
  tiers of competitive Pokemon. 
formattedPokedexes:
  Splits all the Pokemon into Pokedexes divided by their respective tiers (National Dex, AG, Uber, OU, UU, RU, NU, PU, 
  ZU, LC, NFE, CAP).
teamGeneration:
  The random team generator simply samples six unique Pokemon from the master list of Pokemon.
  The stat based team generator returns the six Pokemon with the best respective (hp, atk, def, spa, spd, spe) for each 
  competitive tier, without repeats.
  The combined stat based team generator returns the six pokemon with th ebest respective (phySweep, speSweep, phyTank,
  speTank, wall, total) for each competitive tier, without repeats.
analysis:
  The stats and rankings script compares each of the twelve stats of the pokemon in that specific tier (OU or AG) with 
  its ranking in that tier. Then it plots each data point and draws a linear regression line and calculates a R-squared
  value.
  Multiple JSON files are converted and combined into a useful CSV file that contains the twelve Pokemon stats, its 
  ranking in its respective tiers (OU or AG) as well as its usage in its respective tiers. 
  The prediction script uses that CSV file to train its model to predict the ranks and usages of hypothetical Pokmemon.
