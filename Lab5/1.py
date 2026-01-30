def generuj_raport(imie, stanowisko="Pracownik", miasto="Nieznane"):
    print(f"--- RAPORT PRACOWNIKA ---")
    print(f"Imię: {imie}")
    print(f"Stanowisko: {stanowisko}")
    print(f"Miasto: {miasto}")
    print("-------------------------")

dane_pracownika = {"imie": "Jan", "miasto": "Poznań"}

generuj_raport(**dane_pracownika)