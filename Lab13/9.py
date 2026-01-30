import concurrent.futures
import requests


def pobierz_kurs(waluta):
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json"
    resp = requests.get(url)
    return f"{waluta}: {resp.json()['rates'][0]['mid']}"


waluty = ['EUR', 'USD', 'CHF', 'GBP', 'JPY']

with concurrent.futures.ThreadPoolExecutor() as executor:
    wyniki = executor.map(pobierz_kurs, waluty)

    for wynik in wyniki:
        print(wynik)