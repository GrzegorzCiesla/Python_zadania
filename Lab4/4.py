def generuj_raport(imie, stanowisko="Pracownik", miasto="Nieznane"):
    print(f"--- RAPORT PRACOWNIKA ---")
    print(f"Imię: {imie}")
    print(f"Stanowisko: {stanowisko}")
    print(f"Miasto: {miasto}")
    print("-------------------------")

generuj_raport("Jan")
generuj_raport("Anna", miasto="Kraków")
generuj_raport(miasto="Gdańsk", stanowisko="Kierownik", imie="Piotr")