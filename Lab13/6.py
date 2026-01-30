import multiprocessing
import time


def ciezka_praca(n):
    return sum(i for i in range(n))


if __name__ == "__main__":
    dane = [10_000_000 + i for i in range(8)]

    # Wersja Sekwencyjna
    start = time.perf_counter()
    wyniki_seq = [ciezka_praca(n) for n in dane]
    print(f"Czas sekwencyjny: {time.perf_counter() - start:.2f}s")

    # Wersja Wieloprocesowa
    start = time.perf_counter()
    with multiprocessing.Pool() as pula:
        wyniki_multi = pula.map(ciezka_praca, dane)
    print(f"Czas wieloprocesowy: {time.perf_counter() - start:.2f}s")