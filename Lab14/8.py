def monitor_temperatury(prog_alarmowy):
    suma = 0
    licznik = 0
    srednia = 0.0

    try:
        while True:
            odczyt = yield srednia

            if odczyt is None:
                suma = 0
                licznik = 0
                srednia = 0.0
                print("-> Reset czujnika")
            else:
                suma += odczyt
                licznik += 1
                srednia = suma / licznik

                if srednia > prog_alarmowy:
                    print(f"!!! ALARM: Średnia {srednia:.2f} przekracza {prog_alarmowy} !!!")

    finally:
        print("Czujnik wyłączony")


# Użycie
czujnik = monitor_temperatury(25.0)
next(czujnik)  # Priming

print(f"Średnia: {czujnik.send(20)}")
print(f"Średnia: {czujnik.send(30)}")  # Średnia 25
print(f"Średnia: {czujnik.send(40)}")  # Średnia 30 -> Alarm

czujnik.send(None)  # Reset
print(f"Średnia po resecie: {czujnik.send(10)}")

czujnik.close()