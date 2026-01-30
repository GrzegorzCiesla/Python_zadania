class Ekwipunek:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def pokaz_przedmioty(self):
        print(f"Ekwipunek: {self.przedmioty}")

class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self._hp = hp
        self.ekwipunek = Ekwipunek()

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc

gracz = Gracz("Aragorn", 100)
gracz.ekwipunek.dodaj_przedmiot("Miecz")
gracz.ekwipunek.dodaj_przedmiot("Tarcza")
gracz.ekwipunek.pokaz_przedmioty()