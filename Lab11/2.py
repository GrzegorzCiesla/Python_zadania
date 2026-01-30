from datetime import datetime

# Przygotowanie pliku
with open("wiek.txt", "w") as f:
    f.write("25")


def oblicz_rok_urodzenia(sciezka_pliku):
    try:
        plik = open(sciezka_pliku, "r")
        tekst = plik.read()
        plik.close()

        wiek = int(tekst)
        rok_urodzenia = datetime.now().year - wiek
        print(f"Rok urodzenia: {rok_urodzenia}")

    except FileNotFoundError:
        print("BŁĄD: Nie znaleziono pliku!")
    except ValueError:
        print("BŁĄD: Zawartość pliku nie jest poprawną liczbą!")


# Testowanie
oblicz_rok_urodzenia("wiek.txt")
oblicz_rok_urodzenia("nieistnieje.txt")