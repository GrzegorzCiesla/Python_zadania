from dataclasses import dataclass

@dataclass
class PunktData:
    x: int
    y: int

p1 = PunktData(10, 20)
print(p1)

p2 = PunktData(10, 20)
print(p1 == p2)