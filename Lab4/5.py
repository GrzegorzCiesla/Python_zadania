import math

def oblicz_pole(figura, a=0, b=0, r=0):
    if figura == "prostokat":
        return a * b
    elif figura == "kolo":
        return math.pi * (r ** 2)
    else:
        return None

wynik_prostokat = oblicz_pole("prostokat", a=5, b=10)
print(wynik_prostokat)

wynik_kolo = oblicz_pole("kolo", r=3)
print(wynik_kolo)