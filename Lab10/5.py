from abc import ABC, abstractmethod

# Klasy Gracz, Wojownik, Mag przyjmujemy z Zadania 1
class Gracz:
    def __init__(self, imie): self.imie = imie
    def __repr__(self): return f"Gracz({self.imie})"

class Wojownik(Gracz): pass
class Mag(Gracz): pass

class IFabrykaPostaci(ABC):
    @abstractmethod
    def stworz_postac(self, typ: str, imie: str) -> Gracz:
        pass

class ProstaFabrykaPostaci(IFabrykaPostaci):
    def stworz_postac(self, typ: str, imie: str) -> Gracz:
        if typ == "wojownik":
            return Wojownik(imie)
        elif typ == "mag":
            return Mag(imie)
        else:
            raise ValueError("Nieznany typ")

class ManagerGry:
    def __init__(self, fabryka: IFabrykaPostaci):
        self.fabryka = fabryka

    def rozpocznij_gre(self):
        postac = self.fabryka.stworz_postac("wojownik", "Geralt")
        print(f"Stworzono: {postac}")

# Testowanie
fabryka = ProstaFabrykaPostaci()
manager = ManagerGry(fabryka)
manager.rozpocznij_gre()