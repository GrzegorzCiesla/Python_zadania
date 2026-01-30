import pytest
from portfel import Portfel

@pytest.fixture
def pusty_portfel():
    return Portfel()

def test_poczatkowego_salda(pusty_portfel):
    assert pusty_portfel.saldo == 0

def test_wplaty_do_portfela(pusty_portfel):
    pusty_portfel.wplac(100)
    assert pusty_portfel.saldo == 100