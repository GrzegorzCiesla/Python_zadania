print("Wstęp na kolejkę górską")
wzrost = int(input("Podaj swoj wzrost"))
wiek = int(input("Podaj wiek"))
zgoda = input("Czy posiadasz zgodę opiekuna? (tak/nie)")
if wzrost >= 140 and (wiek >= 18 or zgoda == "tak"):
    print("Mozesz wejsc")
else :
    print("Nie mozesz wejsc")