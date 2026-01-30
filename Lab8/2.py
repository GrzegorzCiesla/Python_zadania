class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def pokaz_status(self):
        print(f"Gracz: {self.imie}, HP: {self.hp}")

    def otrzymaj_obrazenia(self, ilosc):
        self.hp -= ilosc
        print(f"Otrzymano {ilosc} obrażeń.")

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"

    def __repr__(self):
        return f"Gracz(imie='{self.imie}', hp={self.hp})"

gracz = Gracz("Aragorn", 100)
print(gracz)
gracz.pokaz_status()
gracz.otrzymaj_obrazenia(20)
print(gracz)