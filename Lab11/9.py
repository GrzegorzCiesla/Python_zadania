def podmien_imie(sciezka, nowe_imie):
    with open(sciezka, "r+") as plik:
        tresc = plik.read()
        nowa_tresc = tresc.replace("[IMIE]", nowe_imie)
        plik.seek(0)
        plik.write(nowa_tresc)

# Test 1 (krótsze imię)
with open("szablon.txt", "w") as f:
    f.write("Witaj, [IMIE]!")
podmien_imie("szablon.txt", "Anna")
with open("szablon.txt", "r") as f:
    print(f"Wynik Anna: {f.read()}")

# Test 2 (dłuższe imię)
with open("szablon.txt", "w") as f:
    f.write("Witaj, [IMIE]!")
podmien_imie("szablon.txt", "Krzysztof")
with open("szablon.txt", "r") as f:
    print(f"Wynik Krzysztof: {f.read()}")