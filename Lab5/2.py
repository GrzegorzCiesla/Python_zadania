def loguj(funkcja):
    def wrapper():
        print("Start funkcji...")
        funkcja()
        print("Koniec funkcji.")
    return wrapper

@loguj
def przykladowa_funkcja():
    print("To jest treść funkcji.")

przykladowa_funkcja()