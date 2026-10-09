import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def wczytaj_dane(plik):

    df = pd.read_csv(plik , header=None)
    tabela_2d = df.values.tolist()

    return tabela_2d

wynik = wczytaj_dane('dane.csv')
print("Po anglosasku")
print(wynik)

#Spirala

df1 = pd.read_csv('wspolrzedne.csv', header=None)
x = df1[0] #kolumna 1
y = df1[1] #kolumna 2

plt.scatter(x,y, color='blue', marker='x', s=100)
plt.show()

