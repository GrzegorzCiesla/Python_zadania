def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def wykonaj_operacje(a, b, funkcja_operacji):
    return funkcja_operacji(a, b)

wynik_dodawania = wykonaj_operacje(10, 5, dodaj)
wynik_odejmowania = wykonaj_operacje(10, 5, odejmij)

print(wynik_dodawania)
print(wynik_odejmowania)