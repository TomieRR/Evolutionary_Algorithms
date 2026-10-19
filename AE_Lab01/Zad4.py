import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Randomowe zle sudoku 4x4, generowanie randomowych liczb w polach

#wczytanie csv
Wczytane_Sudoku = pd.read_csv('czteroku_11.csv', header=None)
Sudoku = Wczytane_Sudoku.values.tolist()

class GeneratorLosowy:

    def __init__(self):
        self.generator = random.Random()

    def generator_zwroc_calkowita(self,poczatek, koniec):
        return self.generator.randint(poczatek, koniec)

DobryGenerator = GeneratorLosowy()
wyniki = open("Wynik.txt", "w")

Ilosc_prób = 100




for powtorzenia in range(Ilosc_prób):
    Sudoku = Wczytane_Sudoku.values.tolist()
    for wiersze in range(4):
        for kolumny in range(4):
            if Sudoku[wiersze][kolumny] == 0:
                Losowa_liczba = DobryGenerator.generator_zwroc_calkowita(1, 4)
                Sudoku[wiersze][kolumny] = Losowa_liczba
    wyniki.write(str(powtorzenia + 1) + "\n")

    for wiersz in Sudoku:
        linia = (
            str(wiersz[0]) + " " + str(wiersz[1]) + " " + str(wiersz[2]) + " " + str(wiersz[3]) + "\n")
        wyniki.write(linia)
    wyniki.write("\n")

print("Zapisano wyniki")
wyniki.close()