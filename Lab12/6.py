import json

def zapisz_jako_json(dane, sciezka_pliku):
    try:
        with open(sciezka_pliku, "w", encoding="utf-8") as f:
            json.dump(dane, f, indent=4, ensure_ascii=False)
        print("Zapisano pomyślnie.")
    except IOError:
        print("Błąd zapisu.")

moje_dane = {"imie": "Gżegżółka", "id": 123}
zapisz_jako_json(moje_dane, "dane.json")