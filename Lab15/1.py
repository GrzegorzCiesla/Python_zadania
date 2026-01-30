import itertools

# a. Przygotowanie danych (Generatory)
def generator_liter():
    for litera in ['a', 'b', 'c']:
        yield litera

def generator_liczb():
    for liczba in [1, 2, 3]:
        yield liczba

# b. Łączenie strumieni (chain)
polaczony = itertools.chain(generator_liter(), generator_liczb())
print("Połączony strumień:", list(polaczony))

# c. Nieskończony strumień
def nieskonczone_liczby():
    n = 0
    while True:
        yield n
        n += 1

# d. Krojenie (islice) - elementy od indeksu 5 do 14 (czyli 10 elementów)
# islice(iterable, start, stop, step)
kawalek = itertools.islice(nieskonczone_liczby(), 5, 15)
print("Wycinek:", list(kawalek))