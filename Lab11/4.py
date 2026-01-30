class NiepoprawnaIloscProduktuError(ValueError):
    pass

def dodaj_do_koszyka(produkt, ilosc):
    if ilosc <= 0:
        raise NiepoprawnaIloscProduktuError("Ilość produktów musi być dodatnia!")
    print(f"Dodano {ilosc} szt. produktu {produkt}.")

# Testowanie
try:
    dodaj_do_koszyka("Jabłka", 5)
    dodaj_do_koszyka("Gruszki", -2)
except NiepoprawnaIloscProduktuError as e:
    print(e)