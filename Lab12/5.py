import json

# Tworzenie pliku
konfig = {
  "nazwa_hosta": "localhost",
  "port": 8080,
  "debug_mode": True,
  "baza_danych": {"uzytkownik": "admin", "haslo": "tajne"},
  "wspierane_api": ["users", "products"]
}
with open("konfiguracja.json", "w", encoding="utf-8") as f:
    json.dump(konfig, f)

def wczytaj_konfiguracje(sciezka_pliku):
    try:
        with open(sciezka_pliku, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

dane = wczytaj_konfiguracje("konfiguracja.json")
if dane:
    print(dane['baza_danych']['uzytkownik'])