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

class Mag(Gracz):
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Moja mana to {self.mana}.")

druzyna = [
    Gracz("Eowina", 80),
    Wojownik("Aragorn", 150, 25),
    Mag("Gandalf", 100, 50)
]

for postac in druzyna:
    postac.przedstaw_sie()