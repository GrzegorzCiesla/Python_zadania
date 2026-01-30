class Gracz:
    liczba_graczy = 0

    def __init__(self, imie, hp):
        self.imie = imie
        self._hp = hp
        Gracz.liczba_graczy += 1

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc

    def przedstaw_sie(self):
        print(f"Jestem graczem o imieniu {self.imie}.")

# Testowanie
gracz = Gracz("Aragorn", 100)
print(f"Początkowe HP: {gracz.hp}")

gracz.hp = -50
print(f"HP po próbie ustawienia -50: {gracz.hp}")

gracz.hp = 75
print(f"HP po ustawieniu 75: {gracz.hp}")