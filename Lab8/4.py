class Gracz:
    liczba_graczy = 0

    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp
        Gracz.liczba_graczy += 1

    def przedstaw_sie(self):
        print(f"Jestem graczem o imieniu {self.imie}.")

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Moja siła to {self.sila}.")

    def atak(self):
        print(f"Wojownik {self.imie} atakuje z siłą {self.sila}!")

woj = Wojownik("Aragorn", 150, 25)
woj.przedstaw_sie()
woj.atak()