import narzedzia
import time

@narzedzia.mierz_czas
def wolna_funkcja():
    time.sleep(2)

wolna_funkcja()