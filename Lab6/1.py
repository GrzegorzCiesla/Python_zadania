produkty = [
    {"nazwa": "Chleb", "cena": 4.50},
    {"nazwa": "Mleko", "cena": 3.20},
    {"nazwa": "Masło", "cena": 8.99},
    {"nazwa": "Ser", "cena": 15.50}
]

posortowane_produkty = sorted(produkty, key=lambda x: x["cena"])

print(posortowane_produkty)