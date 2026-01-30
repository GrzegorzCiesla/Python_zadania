from abc import ABC, abstractmethod

class StrategiaAtaku(ABC):
    @abstractmethod
    def atakuj(self) -> str:
        pass

class AtakMieczem(StrategiaAtaku):
    def atakuj(self) -> str:
        return "wykonuje szybki cios mieczem!"

class AtakKulaOgnia(StrategiaAtaku):
    def atakuj(self) -> str:
        return "ciska potężną kulą ognia!"

class Gracz:
    def __init__(self, imie, strategia: StrategiaAtaku):
        self.imie = imie
        self.strategia = strategia

    def wykonaj_atak(self):
        print(f"{self.imie} {self.strategia.atakuj()}")

    def zmien_strategie(self, nowa_strategia: StrategiaAtaku):
        self.strategia = nowa_strategia

# Testowanie
gracz = Gracz("Artur", AtakMieczem())
gracz.wykonaj_atak()

gracz.zmien_strategie(AtakKulaOgnia())
gracz.wykonaj_atak()