import json
from pydantic import BaseModel, ValidationError
from typing import List

# Tworzenie pliku
produkt_data = {
  "nazwa_produktu": "Smartfon XYZ",
  "id_produktu": "prod-12345",
  "cena": "1999.99",
  "dostepny": True,
  "tagi": ["elektronika", "nowość"],
  "specyfikacja": {"procesor": "SuperChip", "ram_gb": 8}
}
with open("produkt.json", "w", encoding="utf-8") as f:
    json.dump(produkt_data, f)

class SpecyfikacjaModel(BaseModel):
    procesor: str
    ram_gb: int

class ProduktModel(BaseModel):
    nazwa_produktu: str
    id_produktu: str
    cena: float
    dostepny: bool
    tagi: List[str]
    specyfikacja: SpecyfikacjaModel

def wczytaj_i_waliduj_produkt(sciezka):
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            dane = json.load(f)
            return ProduktModel.parse_obj(dane)
    except (FileNotFoundError, json.JSONDecodeError, ValidationError) as e:
        print(f"Błąd: {e}")
        return None

produkt = wczytaj_i_waliduj_produkt("produkt.json")
if produkt:
    print(produkt.nazwa_produktu)
    print(produkt.specyfikacja.procesor)