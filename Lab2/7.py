while True:
    komenda = input("Podaj komende: ")
    if komenda == "koniec":
        break
    elif komenda.startswith("#"):
        continue