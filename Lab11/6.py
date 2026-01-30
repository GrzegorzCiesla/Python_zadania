import os

class BezpiecznyZapis:
    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.sciezka_tmp = sciezka + ".tmp"

    def __enter__(self):
        self.plik = open(self.sciezka_tmp, "w")
        return self.plik

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        self.plik.close()
        if typ_bledu is None:
            os.replace(self.sciezka_tmp, self.sciezka)
        else:
            if os.path.exists(self.sciezka_tmp):
                os.remove(self.sciezka_tmp)

# Testowanie
with open("konfiguracja.txt", "w") as f:
    f.write("Stara konfiguracja")

with BezpiecznyZapis("konfiguracja.txt") as f:
    f.write("Nowa konfiguracja")

with open("konfiguracja.txt", "r") as f:
    print(f.read())