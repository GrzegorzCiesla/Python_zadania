class Ekwipunek:
    def __init__(self):
        self._przedmioty = {}

    def __len__(self):
        return len(self._przedmioty)

    def __setitem__(self, klucz, wartosc):
        self._przedmioty[klucz] = wartosc

    def __getitem__(self, klucz):
        return self._przedmioty[klucz]

    def __delitem__(self, klucz):
        del self._przedmioty[klucz]

    def __repr__(self):
        return str(self._przedmioty)

    def __iter__(self):
        return iter(self._przedmioty)

    def przegladaj_przedmioty(self):
        print("Otwieranie ekwipunku...")
        for przedmiot in self._przedmioty:
            yield przedmiot
        print("Zamykanie ekwipunku...")

ekwipunek = Ekwipunek()
ekwipunek["miecz"] = 1
ekwipunek["tarcza"] = 1
ekwipunek["mikstura"] = 5

for przedmiot in ekwipunek.przegladaj_przedmioty():
    print(f"Znaleziono: {przedmiot}")