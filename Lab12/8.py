import io
import csv


def generuj_raport_csv_w_pamieci(dane):
    plik_w_pamieci = io.StringIO()
    if not dane:
        return plik_w_pamieci

    pola = list(dane[0].keys())
    writer = csv.DictWriter(plik_w_pamieci, fieldnames=pola)
    writer.writeheader()
    writer.writerows(dane)

    plik_w_pamieci.seek(0)
    return plik_w_pamieci


dane_testowe = [{"col1": "A", "col2": "B"}, {"col1": "C", "col2": "D"}]
plik_ram = generuj_raport_csv_w_pamieci(dane_testowe)
print(plik_ram.read())