from functools import reduce

liczby = [5, 2, 8, 1, 9]

najwieksza = reduce(lambda a, b: a if a > b else b, liczby)

print(najwieksza)