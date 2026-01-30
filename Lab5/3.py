import time

def mierz_czas(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        print(f"Czas wykonania: {koniec - start}")
        return wynik
    return wrapper

@mierz_czas
def czekaj():
    time.sleep(1)

@mierz_czas
def dodaj(a, b):
    return a + b

czekaj()
print(dodaj(10, 20))