import csv

# Przygotowanie pliku
with open("dane.csv", "w", newline='') as f:
    f.write("imie,nazwisko,wiek\nAnna,Kowalska,35\nPiotr,Nowak,41\nZofia,Wisniewska,28\nJan,Jankowski,55")

def czytaj_duzy_csv(sciezka_pliku):
    with open(sciezka_pliku, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['wiek'] = int(row['wiek'])
            yield row

# Test
for osoba in czytaj_duzy_csv("dane.csv"):
    if osoba['wiek'] > 40:
        print(osoba)