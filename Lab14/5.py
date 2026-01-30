import itertools

# Używamy czytaj_duzy_csv z Zadania 3

# Etap 1: Sortowanie (wymagane dla groupby)
zrodlo = czytaj_duzy_csv("dane.csv")
dane_posortowane = sorted(zrodlo, key=lambda x: x['nazwisko'][0])

# Etap 2: Grupowanie
grupy = itertools.groupby(dane_posortowane, key=lambda x: x['nazwisko'][0])

# Etap 3: Agregacja
for litera, grupa in grupy:
    lista_osob = list(grupa)
    srednia_wieku = sum(osoba['wiek'] for osoba in lista_osob) / len(lista_osob)
    print(f"Litera {litera}: średnia {srednia_wieku:.2f}")