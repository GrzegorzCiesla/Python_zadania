class NiewystarczajaceSrodki(Exception):
    pass

class Portfel:
    def __init__(self, saldo_poczatkowe: float = 0) -> None:
        self.saldo: float = saldo_poczatkowe

    def wplac(self, kwota: float) -> None:
        self.saldo += kwota

    def wyplac(self, kwota: float) -> None:
        if kwota > self.saldo:
            raise NiewystarczajaceSrodki()
        self.saldo -= kwota