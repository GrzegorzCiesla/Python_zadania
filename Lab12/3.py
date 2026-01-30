import csv

# Tworzenie pliku do odczytu
with open("pracownicy.csv", "w", encoding="utf-8") as f:
    f.write("imie,stanowisko,pensja\nJan,Programista,8000\nAnna,Manager,12500\nPiotr,Tester,nie_liczba")

def wczytaj_pracownikow(sciezka_pliku):
    wyniki = []
    try:
        with open(sciezka_pliku, "r", newline="", encoding="utf-8") as f:
            czytnik = csv.DictReader(f)
            for wiersz in czytnik:
                try:
                    wiersz['pensja'] = int(wiersz['pensja'])
                    wyniki.append(wiersz)
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Plik nie istnieje")
    return wyniki

pracownicy = wczytaj_pracownikow("pracownicy.csv")
print(pracownicy)