from functools import wraps


# a. Dekorator @korutyna
def korutyna(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)  # Priming
        return gen

    return wrapper


# b. Własny wyjątek
class ResetKorutyny(Exception):
    pass


# c. Korutyna średniej kroczącej
@korutyna
def srednia_kroczaca():
    suma = 0.0
    licznik = 0
    srednia = 0.0

    while True:
        try:
            nowa_liczba = yield srednia
            suma += nowa_liczba
            licznik += 1
            srednia = suma / licznik
        except ResetKorutyny:
            print("-> Resetowanie średniej!")
            suma = 0.0
            licznik = 0
            srednia = 0.0


# d. Testowanie
kalkulator = srednia_kroczaca()
print(f"Średnia (10): {kalkulator.send(10)}")
print(f"Średnia (20): {kalkulator.send(20)}")  # (10+20)/2 = 15.0

kalkulator.throw(ResetKorutyny)
print(f"Średnia po resecie (5): {kalkulator.send(5)}")  # (5)/1 = 5.0