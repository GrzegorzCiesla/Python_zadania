from functools import total_ordering


@total_ordering
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __eq__(self, other):
        if isinstance(other, Gracz):
            return self.imie == other.imie
        return False

    def __lt__(self, other):
        return self.hp < other.hp

    def __repr__(self):
        return f"{self.imie} ({self.hp} HP)"


# Testowanie
g1 = Gracz("Aragorn", 100)
g2 = Gracz("Legolas", 80)

print(f"Czy {g1.imie} > {g2.imie}? {g1 > g2}")
print(f"Czy {g1.imie} <= {g2.imie}? {g1 <= g2}")
print(f"Czy {g1.imie} == {g2.imie}? {g1 == g2}")