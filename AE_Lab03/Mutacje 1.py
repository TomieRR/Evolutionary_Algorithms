import os

import numpy as np
import matplotlib.pyplot as plt


np.random.seed(100)


def ocena_wyniku(os):
    x1 = os[0]
    x2 = os[1]

    wynik = np.sin(x1 * 0.05) + np.sin(x2 * 0.05) + 0.4 * np.sin(x1 * 0.15) * np.sin(x2 * 0.15)

    return wynik

#print(ocena_wyniku([30,70]))

liczba_os = 100

populacja = []

for i in range(liczba_os):
    p = np.random.uniform(0,100)
    d = np.random.uniform(0,100)

    os = [p,d]

    populacja.append(os)
    #print(ocena_wyniku(os))


def mutuj(os, moc):

    os_mut = os.copy()

    p_zmiana = np.random.uniform(-moc,moc)
    d_zmiana = np.random.uniform(-moc,moc)

    os_mut[0] += p_zmiana
    os_mut[1] += d_zmiana

    return os_mut

moc = 5
liczba_lepszych = 0

for os in populacja:
    ocena_przed_mutacja = ocena_wyniku(os)

    zmutowany_osobnik = mutuj(os,moc)

    ocena_po_mutacji = ocena_wyniku(zmutowany_osobnik)

    if ocena_po_mutacji > ocena_przed_mutacja:
        liczba_lepszych += 1

print("Liczba lepszych mutacji: ", liczba_lepszych)

#Najlepszy

najlepszy_os = populacja[0].copy()
najlepsza_ocena = ocena_wyniku(najlepszy_os)

for os in populacja:
    ocena_os = ocena_wyniku(os)

    if ocena_os > najlepsza_ocena:
        najlepszy_os = os.copy()
        najlepsza_ocena = ocena_os

print("Najlepszy osobnik: ", najlepszy_os)
print("Najlepsza ocena: ",najlepsza_ocena)

# 100 mutacji na najlepszym

liczba_mutacji = 100
liczba_lepszych_mutacji = 0
najlepsza_ocena_zmutowanego = None

for numer_proby_mutacji in range(liczba_mutacji):

    zmutowany_osobnik_najlepszego = mutuj(najlepszy_os, moc)

    ocena_po_mutacji_najlepszego = ocena_wyniku(zmutowany_osobnik_najlepszego)

    if ocena_po_mutacji_najlepszego > najlepsza_ocena:
        liczba_lepszych_mutacji += 1

    if najlepsza_ocena_zmutowanego is None:
        najlepsza_ocena_zmutowanego = ocena_po_mutacji_najlepszego

    elif ocena_po_mutacji_najlepszego > najlepsza_ocena_zmutowanego:
        najlepsza_ocena_zmutowanego = ocena_po_mutacji_najlepszego

print("Liczba udanych mutacji najlepszego osobnika:", liczba_lepszych_mutacji)
print("Ocena najlepszego osobnika przed mutacją:", najlepsza_ocena)
print("Najlepsza ocena po mutacji:", najlepsza_ocena_zmutowanego)