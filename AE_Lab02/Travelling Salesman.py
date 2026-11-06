import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

punkty = pd.read_csv("szumoida_10.csv", header=None).to_numpy()

najlepsza_trasa = None
najmniejsza_odleglosc = None

for i in range(400000):
    kolejnosc = np.random.permutation(len(punkty))
    suma = 0
    for j in range(len(kolejnosc)):
        punkt_a = punkty[kolejnosc[j]]
        punkt_b = punkty[kolejnosc[(j+1) % len(kolejnosc)]]
        odleglosc = np.sqrt((punkt_b[0] - punkt_a[0])**2 + (punkt_b[1] - punkt_a[1])**2)
        suma += odleglosc

    if najmniejsza_odleglosc is None or suma < najmniejsza_odleglosc:
        najmniejsza_odleglosc = suma
        najlepsza_trasa = kolejnosc.copy()

print(najmniejsza_odleglosc)
print(najlepsza_trasa)

trasa_z_powrotem = np.append(najlepsza_trasa, najlepsza_trasa[0])
punkty_trasy = punkty[trasa_z_powrotem]


plt.plot(punkty_trasy[:,0], punkty_trasy[:,1])
plt.scatter(punkty_trasy[:,0], punkty_trasy[:,1], color='red')
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()



