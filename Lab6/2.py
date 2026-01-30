oceny = [2, 5, 3, 4, 2]

czy_jest_zagrozenie = any(ocena < 3 for ocena in oceny)
czy_wszystkie_pozytywne = all(ocena >= 3 for ocena in oceny)

print(czy_jest_zagrozenie)
print(czy_wszystkie_pozytywne)