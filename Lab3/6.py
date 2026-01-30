kontakty = {}

while True:
    print("\n--- MENU ---")
    print("1. Dodaj kontakt")
    print("2. Wyświetl kontakt")
    print("3. Usuń kontakt")
    print("4. Wyświetl wszystko")
    print("5. Zakończ")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        nazwa = input("Podaj nazwę: ")
        numer = input("Podaj numer: ")
        kontakty[nazwa] = numer
    elif wybor == "2":
        nazwa = input("Podaj nazwę: ")
        if nazwa in kontakty:
            print(kontakty[nazwa])
        else:
            print("Brak kontaktu w książce.")
    elif wybor == "3":
        nazwa = input("Podaj nazwę: ")
        if nazwa in kontakty:
            del kontakty[nazwa]
            print("Usunięto.")
        else:
            print("Brak kontaktu w książce.")
    elif wybor == "4":
        print("--- MOJE KONTAKTY ---")
        for nazwa, numer in kontakty.items():
            print(f"Nazwa: {nazwa}, Numer: {numer}")
        print("--- KONIEC LISTY ---")
    elif wybor == "5":
        break
    else:
        print("Nieprawidłowy wybór.")