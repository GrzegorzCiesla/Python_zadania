baza_danych = [
    {"imie": "Anna", "stanowisko": "Specjalista", "pensja": 4500},
    {"imie": "Piotr", "stanowisko": "Manager", "pensja": 8000},
    {"imie": "Zofia", "stanowisko": "Specjalista", "pensja": 5200},
    {"imie": "Krzysztof", "stanowisko": "Stażysta", "pensja": 2500}
]

suma_pensji = 0
for pracownik in baza_danych:
    suma_pensji += pracownik["pensja"]

srednia = suma_pensji / len(baza_danych)
print(f"Średnia pensja wszystkich pracowników: {srednia}")

najbogatszy = baza_danych[0]
for pracownik in baza_danych:
    if pracownik["pensja"] > najbogatszy["pensja"]:
        najbogatszy = pracownik

print(f"Najwięcej zarabia: {najbogatszy}")

print("Osoby na stanowisku Specjalista:")
for pracownik in baza_danych:
    if pracownik["stanowisko"] == "Specjalista":
        print(pracownik["imie"])