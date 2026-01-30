import csv


def zapisz_raport_sprzedazy(sciezka_pliku, dane):
    if not dane:
        print("Brak danych.")
        return

    pola = list(dane[0].keys())

    with open(sciezka_pliku, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=pola)
        writer.writeheader()
        writer.writerows(dane)


sprzedaz = [
    {"produkt": "Laptop", "sprzedana_ilosc": 5, "przychody": 15000},
    {"produkt": "Myszka", "sprzedana_ilosc": 20, "przychody": 1000}
]

zapisz_raport_sprzedazy("raport_sprzedazy.csv", sprzedaz)