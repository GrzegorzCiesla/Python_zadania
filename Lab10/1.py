class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __repr__(self):
        return f"{self.__class__.__name__}(imie='{self.imie}', hp={self.hp})"

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def __repr__(self):
        return f"Wojownik(imie='{self.imie}', hp={self.hp}, sila={self.sila})"

class Mag(Gracz):
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def __repr__(self):
        return f"Mag(imie='{self.imie}', hp={self.hp}, mana={self.mana})"

def fabryka_postaci(typ: str, imie: str) -> Gracz:
    if typ == "wojownik":
        return Wojownik(imie, hp=120, sila=25)
    elif typ == "mag":
        return Mag(imie, hp=80, mana=50)
    else:
        raise ValueError(f"Nieznany typ postaci: {typ}")

# Testowanie
wojownik = fabryka_postaci("wojownik", "Aragorn")
mag = fabryka_postaci("mag", "Gandalf")
print(wojownik)
print(mag)

try:
    nieznany = fabryka_postaci("lotr", "Bilbo")
except ValueError as e:
    print(e)