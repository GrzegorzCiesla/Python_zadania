class Portfel:
    def __init__(self, kwota):
        self.kwota = kwota

class Gracz:
    def __init__(self, imie, kwota_startowa):
        self.imie = imie
        self.portfel = Portfel(kwota_startowa)

    def zaplac(self, kwota):
        if self.portfel.kwota >= kwota:
            self.portfel.kwota -= kwota
            print(f"{self.imie} zapłacił {kwota}.")
            return True
        else:
            print(f"{self.imie} nie ma wystarczających środków.")
            return False

# Testowanie
gracz = Gracz("Kupiec", 100)
gracz.zaplac(50)
gracz.zaplac(60)