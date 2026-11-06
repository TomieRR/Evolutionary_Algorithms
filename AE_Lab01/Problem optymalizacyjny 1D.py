import math

import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd



#Mamy funkcję opisaną przez wzór y=sin(x/10)*sin(x/200) (operowanie na radianach a nie
#stopniach). Naszym celem jest znalezienie znalezienie jak najwyższej wartości y, czyli funkcja
#przystosowania to tutaj F(x)=sin(x/… i w tym przykładzie dążymy do maksymalizacji F. Dla
#eksperymentu przyjmuje się, że x mieści się w [0; 100]. Proszę wylosować 20 razy wartość x z
#przedziału [0; 100], następnie proszę podać wartość wszystkich wylosowanych x, następnie wartość
#najlepszego x i y .


class GeneratorLosowy():

    def __init__(self):
        self.generator = random.Random()

    def generator_reset_ziarno(self, liczba):
        self.generator.seed(liczba)

    def generator_reset_losowy(self):
        self.generator.seed()

    def generator_zwroc_calkowita(self, poczatek, koniec):
        return self.generator.randint(poczatek,koniec)

    def generator_zwroc_rzeczywista(self, poczatek, koniec):
        return self.generator.uniform(poczatek,koniec)



DobryGenerator = GeneratorLosowy()
wypisane_liczby = []
wyniki_y = []

#losowanie 20 razy
for i in range(20):
    x = DobryGenerator.generator_zwroc_calkowita(0, 100)
    wypisane_liczby.append(x)
    y = math.sin(x / 10) * math.sin(x / 200)
    wyniki_y.append(y)
#przed posortowaniem X
tablica = np.array(wypisane_liczby)
print(tablica)
#po sortowaniu X
posortowana_tablica_x = np.sort(tablica)[::-1]
print("posortowana_tablica_x",posortowana_tablica_x)

#przed posortowaniem
tablica_y = np.array(wyniki_y)
print(tablica_y)
#po sortowaniu Y
posortowana_tablica_y = np.sort(tablica_y)[::-1]
print("posortowana tablica_y:",posortowana_tablica_y)

#indeks najlepszego
indeks_najlepszego = np.argmax(tablica_y)

najlepsze_x = tablica[indeks_najlepszego]
najlepsze_y = tablica_y[indeks_najlepszego]

print("X dla najlepszej wartosci y: ",najlepsze_x)
print("Najlepsza wartosc y: ",najlepsze_y)

#wykres

plt.figure(figsize=(10,6))

linia_x = np.linspace(0, 100, 30)
linia_y = np.sin(linia_x/10) * np.sin(linia_x/200)

plt.plot(linia_x, linia_y)
plt.scatter(linia_x, linia_y, color='orange')
plt.scatter(najlepsze_x, najlepsze_y, color='red')

plt.show()