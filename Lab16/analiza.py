from kalkulator import srednia

wynik = srednia([1.0, 2.0, 3.0])

if wynik is not None:
    print(f"Wynik + 10 to: {wynik + 10}")
else:
    print("Brak danych do obliczenia średniej.")