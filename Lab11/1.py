# a. Zapis
plik = open("dziennik.txt", "w")
plik.write("Pierwszy wpis.\n")
plik.write("Wszystko działa.\n")
plik.close()

# b. i c. Weryfikacja i Odczyt
plik = open("dziennik.txt", "r")
tresc = plik.read()
print(tresc)
plik.close()

# d. Dopisywanie
plik = open("dziennik.txt", "a")
plik.write("Dodaję kolejną linię.\n")
plik.close()

# Weryfikacja końcowa
plik = open("dziennik.txt", "r")
print(plik.read())
plik.close()