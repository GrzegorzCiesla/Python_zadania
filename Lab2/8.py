slowo = input("Podaj slowo")
licznik_samoglosek = 0
for litera in slowo.lower():
    if litera in "aeiouy":
        licznik_samoglosek += 1
print(licznik_samoglosek)