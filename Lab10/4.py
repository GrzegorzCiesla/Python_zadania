# Wymaga klasy StrategiaAtaku i Gracz z Zadania 2

class StaryBohater:
    def wykonaj_uderzenie(self) -> str:
        return "Stary bohater wykonuje potężne uderzenie!"

class AdapterBohatera(StrategiaAtaku):
    def __init__(self, stary_bohater: StaryBohater):
        self.stary_bohater = stary_bohater

    def atakuj(self) -> str:
        return self.stary_bohater.wykonaj_uderzenie()

# Testowanie
stary_heros = StaryBohater()
adapter = AdapterBohatera(stary_heros)
nowy_gracz = Gracz("Zadaptowany", adapter)

nowy_gracz.wykonaj_atak()