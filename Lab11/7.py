def zlicz_bledy(sciezka_pliku):
    licznik = 0
    try:
        with open(sciezka_pliku, "r") as plik:
            for linia in plik:
                try:
                    czesc = linia.strip().split(':', 1)
                    if len(czesc) == 2 and czesc[0] == "ERROR":
                        licznik += 1
                except ValueError:
                    continue
    except FileNotFoundError:
        return 0
    return licznik

# Utworzenie pliku testowego
with open("log.txt", "w") as f:
    f.write("INFO:Start\nERROR:Błąd 1\nZła linia\nERROR:Błąd 2\n")

print(f"Liczba błędów: {zlicz_bledy('log.txt')}")