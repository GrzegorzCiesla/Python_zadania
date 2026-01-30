from typing import List, Optional

def dodaj(a: float, b: float) -> float:
    return a + b

def dziel(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b

def srednia(liczby: List[float]) -> Optional[float]: # Python 3.10+ można użyć: float | None
    if not liczby:
        return None
    return sum(liczby) / len(liczby)