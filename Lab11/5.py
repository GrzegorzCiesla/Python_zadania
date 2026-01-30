import time

class MiernikCzasu:
    def __enter__(self):
        print("Rozpoczynam pomiar.")
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.koniec = time.perf_counter()
        czas_trwania = self.koniec - self.start
        print(f"Czas trwania: {czas_trwania:.5f} sek.")

# Testowanie
with MiernikCzasu():
    suma = sum(n for n in range(1_000_000))