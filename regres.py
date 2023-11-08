import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#import punktów
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

#Wyodrębniamy dane z wejścia
X = df.values[:, :-1]

#Wyodrębniamy wyjście
Y = df.values[:, -1]

#regresja
dopasowanie = LinearRegression().fit(X, Y)

m = dopasowanie.coef_.flatten()
b = dopasowanie.intercept_.flatten()

print("m = {0}".format(m))
print("b = {0}".format(b))

#Pokazanie na wykresie
plt.plot(X, Y, 'o')
plt.plot(X, m*X+b)
plt.show()