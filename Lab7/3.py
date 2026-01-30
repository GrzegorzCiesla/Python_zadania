pracownicy = [
    {"imie": "Anna", "stanowisko": "Specjalista", "pensja": 4500},
    {"imie": "Piotr", "stanowisko": "Manager", "pensja": 8000},
    {"imie": "Zofia", "stanowisko": "Specjalista", "pensja": 5200},
]

lista_plac = [p["pensja"] for p in pracownicy if p["stanowisko"] == "Specjalista"]

print(f"Lista płac dla specjalistów: {lista_plac}")