class NieujemnaLiczba:
    def __set_name__(self, owner, name):
        self._nazwa_atrybutu = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self._nazwa_atrybutu)

    def __set__(self, instance, value):
        if value < 0:
            instance.__dict__[self._nazwa_atrybutu] = 0
        else:
            instance.__dict__[self._nazwa_atrybutu] = value

class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

class Wojownik(Gracz):
    sila = NieujemnaLiczba()
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

class Mag(Gracz):
    mana = NieujemnaLiczba()
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

# Testowanie
w = Wojownik("Aragorn", 100, -10)
m = Mag("Gandalf", 80, -50)

print(f"Wojownik sila: {w.sila}")
print(f"Mag mana: {m.mana}")

w.sila = 25
print(f"Wojownik sila po zmianie: {w.sila}")