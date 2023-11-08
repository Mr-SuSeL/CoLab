import pandas as pd

# Importujemy punktu
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",").itertuples()

# Testujemy wybrana linię - wyniki z regresji liniowej
m = 1.93939
b = 4.73333

# Obliczamy reszty
for p in points:
    y_rzeczywista = p.y
    y_przewidywana = m*p.x + b
    reszta = y_rzeczywista - y_przewidywana
    print(reszta)