class LicznikJednorazowy:
    def __init__(self, max_val):
        self.max = max_val
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            wynik = self.n
            self.n += 1
            return wynik
        else:
            raise StopIteration

# Eksperyment
licznik = LicznikJednorazowy(3)

print("Pętla 1:")
for i in licznik:
    print(i)

print("Pętla 2:")
for i in licznik:
    print(i)
# Wniosek: Druga pętla nic nie wypisze, bo iterator jest zużyty (self.n wynosi 3).