class BrakPunktowZyciaError(Exception):
    pass

class Wojownik:
    def __init__(self, imie, hp, sila):
        self.imie = imie
        self.hp = hp
        self.sila = sila

    def atakuj(self):
        if self.hp <= 0:
            raise BrakPunktowZyciaError("Postać nie może atakować!")
        print(f"Wojownik {self.imie} atakuje!")

# Testowanie
try:
    wojownik = Wojownik("Bjorn", 0, 20)
    wojownik.atakuj()
except BrakPunktowZyciaError as e:
    print(e)