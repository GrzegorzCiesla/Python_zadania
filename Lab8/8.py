class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def przedstaw_sie(self):
        print(f"Jestem graczem o imieniu {self.imie}.")

    @staticmethod
    def sprawdz_poprawnosc_imienia(imie):
        return bool(imie and imie[0].isupper())

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Moja siła to {self.sila}.")

    @classmethod
    def stworz_berserkera(cls, imie):
        return cls(imie, hp=80, sila=40)

# Testowanie
berserker = Wojownik.stworz_berserkera("Olaf")
berserker.przedstaw_sie()

print(Gracz.sprawdz_poprawnosc_imienia("Aragorn"))
print(Gracz.sprawdz_poprawnosc_imienia("aragorn"))
print(Gracz.sprawdz_poprawnosc_imienia(""))