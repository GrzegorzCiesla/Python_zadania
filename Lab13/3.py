import threading
import time
import requests

def pobierz_kurs(waluta):
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json"
    print(f"Pobieranie kursu dla {waluta}...")
    try:
        resp = requests.get(url)
        dane = resp.json()
        print(f"Kurs {waluta}: {dane['rates'][0]['mid']}")
    except Exception as e:
        print(f"Błąd dla {waluta}: {e}")

waluty = ['EUR', 'USD', 'CHF', 'GBP', 'JPY']

# Wersja Sekwencyjna
start_seq = time.perf_counter()
for w in waluty:
    pobierz_kurs(w)
koniec_seq = time.perf_counter()
print(f"Czas sekwencyjny: {koniec_seq - start_seq:.2f}s")

# Wersja Wielowątkowa
print("\nRozpoczynam wersję wielowątkową...")
watki = []
start_par = time.perf_counter()

for w in waluty:
    watek = threading.Thread(target=pobierz_kurs, args=(w,))
    watki.append(watek)
    watek.start()

for watek in watki:
    watek.join()

koniec_par = time.perf_counter()
print(f"Czas wielowątkowy: {koniec_par - start_par:.2f}s")