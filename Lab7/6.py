def znajdz_wartosc(dane, szukany_klucz):
    for klucz, wartosc in dane.items():
        if klucz == szukany_klucz:
            return wartosc
        if isinstance(wartosc, dict):
            wynik = znajdz_wartosc(wartosc, szukany_klucz)
            if wynik is not None:
                return wynik
    return None

dane_przyklad = {
    "uzytkownik": "Jan",
    "ustawienia": {
        "powiadomienia": "tak",
        "zaawansowane": {
            "klucz_api": "tajny_kod_123",
            "limit": 100
        }
    }
}

print(znajdz_wartosc(dane_przyklad, "klucz_api"))