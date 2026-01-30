class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def przedstaw_sie(self):
        print(f"Jestem graczem o imieniu {self.imie}.")

    def __eq__(self, other):
        if isinstance(other, Gracz):
            return self.imie == other.imie
        return False

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        print(f"Wojownik: {self.imie}, HP: {self.hp}, Siła: {self.sila}")

    def __add__(self, other):
        nowe_imie = f"{self.imie} i {other.imie}"
        nowe_hp = self.hp + other.hp
        nowa_sila = self.sila + other.sila
        return Wojownik(nowe_imie, nowe_hp, nowa_sila)

# Testowanie __eq__
g1 = Gracz("Aragorn", 100)
g2 = Gracz("Aragorn", 100)
print(f"Czy g1 == g2? {g1 == g2}")

# Testowanie __add__
w1 = Wojownik("Aragorn", 150, 25)
w2 = Wojownik("Boromir", 140, 30)
fuzja = w1 + w2
fuzja.przedstaw_sie()