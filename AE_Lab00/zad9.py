import random



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
        return self.generator.uniform(poczatek,koniec) #uniform to liczba po przecinku, float z przedzialu

    def generator_zwroc_permutacje(self, size):
        tablica = list(range(size))
        self.generator.shuffle(tablica) #shuffle tasuje liczby z tablicy
        return tablica

    ########

SprytnyGenerator = GeneratorLosowy()

test1 = SprytnyGenerator.generator_reset_ziarno(123)
test2 = SprytnyGenerator.generator_zwroc_calkowita(-100,100)
test3 = SprytnyGenerator.generator_zwroc_rzeczywista(0,100)
test4 = SprytnyGenerator.generator_reset_ziarno(123)
test5 = SprytnyGenerator.generator_zwroc_calkowita(-100,100)
test6 = SprytnyGenerator.generator_reset_losowy()
test7 = SprytnyGenerator.generator_zwroc_calkowita(-100,100)

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)

print("Czy są wyniki są takie same?")

if int(test2) == int(test5):
    print(True)
else:
    print(False)
print("----------")
print("Zawsze randomowa liczba: ", test7)
