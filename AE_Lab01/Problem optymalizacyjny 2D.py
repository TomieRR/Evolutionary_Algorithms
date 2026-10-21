import math
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Mamy funkcję opisaną przez wzór F(x1,x2)=sin(x1*0.05) +sin(x2*0.05) +0.4*sin(x1*0.15)*sin(x2*0.15)
#(operowanie na radianach a nie stopniach) , przedział zmienności x1 i x2 to [0; 100].
#Proszę 20 do 100 razy wylosować wartości x1 i x2, następnie proszę podać wartość
#najlepszej pary (x1; x2) i funkcji przystosowania dla nich wyliczonych.


class GeneratorLosowy():
    def __init__(self):
        self.generator = random.Random()

    def generator_reset_ziarno(self):
        self.generator.seed()

    def generator_liczb_calkowitych_w_przedziale(self, poczatek, koniec):
        return self.generator.randint(poczatek,koniec)

    def generator_liczb_rzeczywistych_w_przedziale(self, poczatek, koniec):
        return self.generator.uniform(poczatek,koniec)


Generatorek = GeneratorLosowy()

Lista_x1 = []
Lista_x2 = []
wyniki_funkcji = []


for i in range(67):
    #ewentualnie
    #x1 = Generatorek.generator_liczb_rzeczywistych_w_przedziale(0, 100)
    #x2 = Generatorek.generator_liczb_rzeczywistych_w_przedziale(0, 100)
    x1 = Generatorek.generator_liczb_calkowitych_w_przedziale(0,100)
    x2 = Generatorek.generator_liczb_calkowitych_w_przedziale(0, 100)

    f = math.sin(x1*0.05) + math.sin(x2*0.05) + 0.4 * math.sin(x1*0.15)*math.sin(x2*0.15)

    Lista_x1.append(x1)
    Lista_x2.append(x2)
    wyniki_funkcji.append(f)

tablica_x1 = np.array(Lista_x1)
tablica_x2 = np.array(Lista_x2)
tablica_wyniki_funkcji = np.array(wyniki_funkcji)

indeks_najlepszego1 = np.argmax(tablica_wyniki_funkcji)
najlepsze_x1 = tablica_x1[indeks_najlepszego1]
najlepsze_x2 = tablica_x2[indeks_najlepszego1]
najlepszy_wynik_funkcji = tablica_wyniki_funkcji[indeks_najlepszego1]

print("Wszystkie X1: ",Lista_x1)
print("Wszystkie X2: ",Lista_x2)
print("Wszystkie wyniki: ",wyniki_funkcji)
print("Najlepsza para (x1,x2): ", najlepsze_x1, najlepsze_x2)
print("Najlepszy wynik funkcji: ", najlepszy_wynik_funkcji)

linia_x1 = np.linspace(0, 100, 67)
linia_x2 = np.linspace(0, 100, 67)

x1, x2 = np.meshgrid(linia_x1, linia_x2)
Funkcja = np.sin(x1*0.05) + np.sin(x2*0.05) + 0.4 * np.sin(x1*0.15)*np.sin(x2*0.15)

fig = plt.figure(figsize=(10,6))
plt.contour(x1,x2,Funkcja, levels=20, colors='k')
plt.scatter(tablica_x1, tablica_x2)
plt.scatter(najlepsze_x1,najlepszy_wynik_funkcji, color='red')

plt.xlabel("X1")
plt.ylabel("X2")
plt.show()