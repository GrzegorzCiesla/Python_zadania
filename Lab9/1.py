class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __repr__(self):
        return f"{self.imie} ({self.hp} HP)"

    def __lt__(self, other):
        return self.hp < other.hp

# Testowanie
lista_graczy = [
    Gracz("Gimli", 120),
    Gracz("Legolas", 80),
    Gracz("Aragorn", 100)
]

posortowani = sorted(lista_graczy)
print(posortowani)