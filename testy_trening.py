import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://bit.ly/3cIH97A', delimiter = ",")

X = df.values[:, :-1]
Y = df.values[:, -1]

X_trening, X_test, Y_trening, Y_test = train_test_split(X, Y, test_size=1/3)

model = LinearRegression()
model.fit(X_trening, Y_trening)
wynik = model.score(X_test, Y_test)
print("r^2: %.3f" % wynik)