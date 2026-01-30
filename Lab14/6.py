import itertools

zrodlo = czytaj_duzy_csv("dane.csv")

# Rozdzielenie strumienia
iter1, iter2 = itertools.tee(zrodlo, 2)

# Analiza 1: Najdłuższe imię i nazwisko
najdluzsza_osoba = max(iter1, key=lambda x: len(x['imie'] + x['nazwisko']))
print(f"Najdłuższe imię i nazwisko: {najdluzsza_osoba['imie']} {najdluzsza_osoba['nazwisko']}")

# Analiza 2: Liczba osób i łączny wiek
lista_osob = list(iter2)
liczba_osob = len(lista_osob)
laczny_wiek = sum(x['wiek'] for x in lista_osob)
print(f"Liczba osób: {liczba_osob}, Łączny wiek: {laczny_wiek}")