import pytest
from kalkulator import dodaj, dziel, srednia

@pytest.mark.parametrize("a, b, wynik", [
    (2, 3, 5),
    (-2, -3, -5),
    (-2, 3, 1),
    (5, 0, 5)
])
def test_dodawania_wielu_przypadkow(a, b, wynik):
    assert dodaj(a, b) == wynik

def test_dzielenia_przez_zero_powinno_rzucic_blad():
    with pytest.raises(ValueError):
        dziel(10, 0)

def test_poprawnego_dzielenia():
    assert dziel(10, 2) == 5.0

def test_srednia_poprawna():
    assert srednia([1.0, 2.0, 3.0]) == 2.0

def test_srednia_pusta_lista():
    assert srednia([]) is None