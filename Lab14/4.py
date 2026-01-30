# Używamy funkcji czytaj_duzy_csv z poprzedniego zadania

# Etap 1: Filtr (osoby > 30 lat)
zrodlo = czytaj_duzy_csv("dane.csv")
osoby_po_30 = (osoba for osoba in zrodlo if osoba['wiek'] > 30)

# Etap 2: Transformacja (imię i nazwisko upper)
opisy = (f"{osoba['imie']} {osoba['nazwisko']}".upper() for osoba in osoby_po_30)

# Etap 3: Konsumpcja
for opis in opisy:
    print(opis)