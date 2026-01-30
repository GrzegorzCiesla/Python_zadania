def rozdziel_imie_nazwisko(imie_i_nazwisko):
    rozdzielone = imie_i_nazwisko.split()
    return rozdzielone[0], rozdzielone[1]

imie, nazwisko = rozdziel_imie_nazwisko("Jan Kowalski")
print(imie)
print(nazwisko)