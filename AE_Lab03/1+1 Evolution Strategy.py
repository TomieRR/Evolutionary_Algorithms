import numpy as np
import matplotlib.pyplot as plt

def funkcja(x):
    return np.sin(x / 10) * np.sin(x / 200)

np.random.seed(10)

moc = 5
iteracje = 20


x_min = 0
x_max = 100

x_rn = 35 #right now
y_rn = funkcja(x_rn)

lista_x_rn = []
lista_x_m = []

lista_y_rn = []
lista_y_m = []

for i in range(iteracje):
    mutacja = np.random.uniform(-moc, moc)
    x_m = x_rn + mutacja

    y_m = funkcja(x_m)

    if y_m > y_rn:
        x_rn = x_m
        y_rn = y_m

lista_x_rn.append(x_rn)
lista_x_m.append(x_m)
lista_y_rn.append(y_rn)
lista_y_m.append(y_m)

print("Najlepsze x: ", x_rn)
print("Wartosc funkcji: ", y_rn)