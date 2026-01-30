class MenedzerKonfiguracji:
    _instancja = None
    _zainicjalizowany = False

    def __new__(cls):
        if cls._instancja is None:
            cls._instancja = super().__new__(cls)
        return cls._instancja

    def __init__(self):
        if self._zainicjalizowany:
            return
        self.ustawienia = {"trudnosc": "normalna"}
        self._zainicjalizowany = True

# Testowanie
config1 = MenedzerKonfiguracji()
config2 = MenedzerKonfiguracji()

print(f"Czy to ten sam obiekt? {config1 is config2}")
config1.ustawienia["trudnosc"] = "trudna"
print(config2.ustawienia)