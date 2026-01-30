# a. Zapis z with
with open("dziennik_with.txt", "w") as plik:
    plik.write("Pierwszy wpis.\n")
    plik.write("Wszystko działa.\n")

# b. Odczyt z with
with open("dziennik_with.txt", "r") as plik:
    print(plik.read())

# c. Dopisywanie z with
with open("dziennik_with.txt", "a") as plik:
    plik.write("Dodaję kolejną linię.\n")

# d. Weryfikacja
with open("dziennik_with.txt", "r") as plik:
    print(plik.read())