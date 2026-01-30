from abc import ABC, abstractmethod

class IObserwator(ABC):
    @abstractmethod
    def aktualizuj(self, wiadomosc: str):
        pass

class Gracz(IObserwator):
    def __init__(self, imie):
        self.imie = imie

    def aktualizuj(self, wiadomosc: str):
        print(f"Gracz {self.imie} otrzymał powiadomienie: {wiadomosc}")

class SerwerGry:
    def __init__(self):
        self._obserwatorzy = []

    def dodaj_obserwatora(self, obserwator: IObserwator):
        self._obserwatorzy.append(obserwator)

    def powiadom_wszystkich(self, wiadomosc: str):
        for obs in self._obserwatorzy:
            obs.aktualizuj(wiadomosc)

# Testowanie
serwer = SerwerGry()
g1 = Gracz("Jan")
g2 = Gracz("Anna")

serwer.dodaj_obserwatora(g1)
serwer.dodaj_obserwatora(g2)
serwer.powiadom_wszystkich("Nowy boss się pojawił!")