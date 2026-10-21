from email.header import Header

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Dane = pd.read_csv("szumoida_10.csv", header=None)

x = Dane.iloc[:,0].to_numpy()
y = Dane.iloc[:,1].to_numpy()

np.random.seed(10) #te same dane

najlepsze_a = None
najlepsze_b = None
najmniejsze_mae = None

for i in range(300):
    a = np.random.uniform(3,11)
    b = np.random.uniform(10,40)
    wyliczony_y = a * np.sin(x/b)
    bledy = np.abs(y-wyliczony_y)
    mae = np.mean(bledy)
    if najmniejsze_mae is None or mae < najmniejsze_mae:
        najlepsze_a = a
        najlepsze_b = b
        najmniejsze_mae = mae

print(najlepsze_a)
print(najlepsze_b)
print(najmniejsze_mae)

x_wykres = np.linspace(x.min(),x.max(),500)
y_wykres = najlepsze_a* np.sin(x_wykres/najlepsze_b)

plt.scatter(x,y, color='blue', label='Dane z csv')
plt.plot(x_wykres,y_wykres,color='red', label='Najlepsza funkcja')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()