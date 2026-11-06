import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# randomowe zle sudoku 4x4, generowanie randomowych liczb w polach = 0

# wczytanie csv i zapisanie jako lista do porownywania
Wczytane_Sudoku = pd.read_csv('czteroku_11.csv', header=None)
Oryginalne_Sudoku = Wczytane_Sudoku.values.tolist()


class GeneratorLosowy:

    def __init__(self):
        self.generator = random.Random()

    def generator_zwroc_calkowita(self, poczatek, koniec):
        return self.generator.randint(poczatek, koniec)


DobryGenerator = GeneratorLosowy()
wyniki = open("Wynik.txt", "w")

Ilosc_prob = 100

# zmienne do zapamietywania najlepszego wyniku
Najmniejsza_ilosc_bledow = 13  # aby pierwsze sudoku nadpisywalo od razu ta liczbe
Najlepsze_sudoku = []

for powtorzenia in range(Ilosc_prob):

    Sudoku = [wiersz[:] for wiersz in Oryginalne_Sudoku]

    # generowanie sudoku
    for wiersze in range(4):
        for kolumny in range(4):
            if Sudoku[wiersze][kolumny] == 0:
                Losowa_liczba = DobryGenerator.generator_zwroc_calkowita(1, 4)
                Sudoku[wiersze][kolumny] = Losowa_liczba

    # zliczanie bledow
    Ilosc_bledow = 0

    # wiersze
    for indeks_wiersza in range(4):
        Wiersz = Sudoku[indeks_wiersza]
        Czy_wiersz_ma_blad = False

        for liczba_do_sprawdzenia in range(1, 5):
            if Wiersz.count(liczba_do_sprawdzenia) > 1:
                Czy_wiersz_ma_blad = True

        if Czy_wiersz_ma_blad == True:
            Ilosc_bledow = Ilosc_bledow + 1

    # kolumny
    for indeks_kolumny in range(4):
        Kolumna = []
        for indeks_wiersza in range(4):
            Kolumna.append(Sudoku[indeks_wiersza][indeks_kolumny])

        Czy_kolumna_ma_blad = False
        for liczba_do_sprawdzenia in range(1, 5):
            if Kolumna.count(liczba_do_sprawdzenia) > 1:
                Czy_kolumna_ma_blad = True

        if Czy_kolumna_ma_blad == True:
            Ilosc_bledow = Ilosc_bledow + 1

    # Bloki
    for poczatek_wiersza_bloku in [0, 2]:
        for poczatek_kolumny_bloku in [0, 2]:
            Blok = []
            for indeks_wiersza in range(poczatek_wiersza_bloku, poczatek_wiersza_bloku + 2):
                for indeks_kolumny in range(poczatek_kolumny_bloku, poczatek_kolumny_bloku + 2):
                    Blok.append(Sudoku[indeks_wiersza][indeks_kolumny])

            Czy_blok_ma_blad = False
            for liczba_do_sprawdzenia in range(1, 5):
                if Blok.count(liczba_do_sprawdzenia) > 1:
                    Czy_blok_ma_blad = True

            if Czy_blok_ma_blad == True:
                Ilosc_bledow = Ilosc_bledow + 1

    # sprawdzenie czy sudoku jest lepsze
    if Ilosc_bledow < Najmniejsza_ilosc_bledow:
        Najmniejsza_ilosc_bledow = Ilosc_bledow
        # kopiowanie listy, aby przy petli nie zanikala
        Najlepsze_sudoku = [wiersz[:] for wiersz in Sudoku]

    # zapisywanie do pliku
    wyniki.write(str(powtorzenia + 1) + " | bledy: " + str(Ilosc_bledow) + "\n")

    for wiersz in Sudoku:
        linia = (str(wiersz[0]) + " " + str(wiersz[1]) + " " + str(wiersz[2]) + " " + str(wiersz[3]) + "\n")
        wyniki.write(linia)
    wyniki.write("\n")

    # przerwanie petli jesli nie bedzie bledow
    if Ilosc_bledow == 0:
        print("znaleziono sudoku z 0 bledami! przerywam petle przy probie: " + str(powtorzenia + 1))
        break

print("zapisano wyniki")
wyniki.close()

# wypisanie najlepszego wyniku
print("\nnajlepsze znalezione sudoku mialo bledow: " + str(Najmniejsza_ilosc_bledow))
for wiersz in Najlepsze_sudoku:
    print(str(wiersz[0]) + " " + str(wiersz[1]) + " " + str(wiersz[2]) + " " + str(wiersz[3]))