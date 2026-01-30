def generuj_raport(**szczegoly):
    for klucz, wartosc in szczegoly.items():
        print(f"{klucz}: {wartosc}")

generuj_raport(status="Aktywny", punkty=150)
generuj_raport(imie="Anna", kraj="Polska", wiek=30)