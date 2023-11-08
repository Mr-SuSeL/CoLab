import pandas as pd

punkty = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())
# Budujemy model
m = 0.0
b = 0.0

# Tempo nauki
L = .001

# Liczba iteracji
iteracje = 100_000

n = float(len(punkty)) #liczba el.w X

# Gradient prosty
for i in range(iteracje):
    # Nachylenie względem m
    D_m = sum(2 * p.x * ((m * p.x + b) - p.y) for p in punkty)

    # Nachylenie względem b
    D_b = sum(2 * ((m * p.x + b) - p.y) for p in punkty)

    # Aktualizujemy m i b
    m -= L * D_m
    b -= L * D_b

print("y = {0}x + {1}".format(m, b))