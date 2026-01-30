wiek = int(input("Podaj wiek: "))
if wiek < 13:
    print("Jestes dzieckiem")
elif wiek < 18:
    print("Jestes nastolatkiem")
elif wiek < 65:
    print("Jestes doroslym")
else:
    print("Jestes seniorem")