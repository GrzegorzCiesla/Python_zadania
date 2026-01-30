wprowadzone_dane = input("Podaj listę tagów oddzielonych przecinkami: ")

surowe_tagi = wprowadzone_dane.split(',')

czyste_tagi = []

for i in surowe_tagi:
    oczyszczony_tag = i.strip()
    czyste_tagi.append(oczyszczony_tag)

unikalne_tagi = set(czyste_tagi)

liczba_wszystkich = len(czyste_tagi)

liczba_unikalnych = len(unikalne_tagi)


print(f"Liczba wszystkich podanych tagów: {liczba_wszystkich}")
print(f"Liczba unikalnych tagów: {liczba_unikalnych}")
print()


print("Unikalne tagi (alfabetycznie):")

for i in sorted(unikalne_tagi):
    print(f"- {i}")