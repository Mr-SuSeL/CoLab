from scipy.stats import t
#rozkład t bo mniej niż 31 próbek
from math import sqrt

n = 10
# Sprawdzamy 92% przedział ufności z obu stron czyli po 2.5%
dolna_wk = t(n-1).ppf(.025)
gorna_wk = t(n-1).ppf(.975)
# print(dolna_wk, gorna_wk)

# Współczynnik korelacji wcześniej liczony:
r = 0.957586

# Test
wartosc_testowa = r / sqrt((1 - r**2) / (n - 2))

print("Wartość testowa: {}".format(wartosc_testowa))
print("Zakres krytyczny: {}, {}".format(dolna_wk, gorna_wk))

if wartosc_testowa < dolna_wk or wartosc_testowa > gorna_wk:
    print("Korelacja potwierdzona, można odrzucić hipotezę zerową")
else:
    print("Korelacja niepotwierdzona")

# Obliczamy wartość p
if wartosc_testowa > 0:
    wartosc_p = 1.0 - t(n-1).cdf(wartosc_testowa)
else:
    wartosc_p = t(n-1).cdf(wartosc_testowa)

print("Wartość testowa:", wartosc_testowa)

# Test dwustronny więc mnożymy przez 2
wartosc_p *= 2
# p ma być poniżej 5%
print("Wartość P: {}".format(wartosc_p)) 


