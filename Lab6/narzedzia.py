import time

def mierz_czas(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        print(f"Czas wykonania: {koniec - start} s")
        return wynik
    return wrapper