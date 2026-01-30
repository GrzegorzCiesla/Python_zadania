class Gracz:
    liczba_graczy = 0

    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp
        Gracz.liczba_graczy += 1

    def pokaz_status(self):
        print(f"Gracz: {self.imie}, HP: {self.hp}")

    def otrzymaj_obrazenia(self, ilosc):
        self.hp -= ilosc
        print(f"Otrzymano {ilosc} obrażeń.")

    def __str__(self):
        return f"Gracz {self.imie} (HP: {self.hp})"

    def __repr__(self):
        return f"Gracz(imie='{self.imie}', hp={self.hp})"

print(Gracz.liczba_graczy)

g1 = Gracz("Aragorn", 100)
g2 = Gracz("Legolas", 80)
g3 = Gracz("Gimli", 120)

print(Gracz.liczba_graczy)