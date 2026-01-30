from functools import wraps


def korutyna(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return wrapper


class ResetProcesora(Exception):
    pass


@korutyna
def procesor_polecen():
    dane = []
    print("Procesor gotowy.")

    while True:
        try:
            polecenie = yield

            # Parsowanie "AKCJA:WARTOŚĆ"
            czesci = polecenie.split(":", 1)
            akcja = czesci[0].upper()
            wartosc = czesci[1] if len(czesci) > 1 else None

            if akcja == "DODAJ":
                if wartosc:
                    dane.append(wartosc)
                    print(f"Dodano: {wartosc}")
            elif akcja == "USUN":
                if wartosc in dane:
                    dane.remove(wartosc)
                    print(f"Usunięto: {wartosc}")
                else:
                    print(f"Brak wartości: {wartosc}")
            elif akcja == "POKAZ":
                print(f"Stan: {dane}")
            else:
                print("Nieznana komenda")

        except ResetProcesora:
            print("!!! RESET PROCESORA !!!")
            dane = []


# Testowanie
proc = procesor_polecen()
proc.send("DODAJ:Mleko")
proc.send("DODAJ:Chleb")
proc.send("POKAZ")
proc.send("USUN:Mleko")
proc.send("POKAZ")

proc.throw(ResetProcesora)
proc.send("POKAZ")