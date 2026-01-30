from abc import ABC, abstractmethod

class Bohater(ABC):
    @abstractmethod
    def atak(self) -> int:
        pass

    @abstractmethod
    def opis(self) -> str:
        pass

class Wojownik(Bohater):
    def atak(self) -> int:
        return 10

    def opis(self) -> str:
        return "Wojownik"

class DekoratorBohatera(Bohater):
    def __init__(self, bohater: Bohater):
        self.bohater = bohater

    def atak(self) -> int:
        return self.bohater.atak()

    def opis(self) -> str:
        return self.bohater.opis()

class MagicznyMiecz(DekoratorBohatera):
    def atak(self) -> int:
        return super().atak() + 5

    def opis(self) -> str:
        return super().opis() + ", z magicznym mieczem"

class OgnistaZbroja(DekoratorBohatera):
    def atak(self) -> int:
        return super().atak() + 2

    def opis(self) -> str:
        return super().opis() + ", w ognistej zbroi"

# Testowanie
bohater = Wojownik()
bohater = MagicznyMiecz(bohater)
bohater = OgnistaZbroja(bohater)

print(f"{bohater.opis()} -> Atak: {bohater.atak()}")