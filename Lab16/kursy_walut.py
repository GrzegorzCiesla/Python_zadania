import requests

def pobierz_cene_euro():
    response = requests.get("http://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json")
    data = response.json()
    return data['rates'][0]['mid']