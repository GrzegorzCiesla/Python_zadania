class Odliczanie:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # Implementacja __iter__ jako generatora
        liczba = self.start
        while liczba > 0:
            yield liczba
            liczba -= 1
        yield "START!"

# Testowanie
odliczanie = Odliczanie(3)
for x in odliczanie:
    print(x)

print("Drugi raz:")
for x in odliczanie:
    print(x)