class OtwarcieSkrzyni:
    def __enter__(self):
        print("Otwieram skrzynię...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Zamykam skrzynię...")

with OtwarcieSkrzyni():
    print("Przeglądam łupy...")