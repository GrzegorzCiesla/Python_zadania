class IgnorujBledy:
    def __init__(self, bledy_do_ignorowania):
        self.bledy_do_ignorowania = bledy_do_ignorowania

    def __enter__(self):
        pass

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        if typ_bledu and issubclass(typ_bledu, self.bledy_do_ignorowania):
            print(f"Zignorowano błąd: {typ_bledu.__name__}")
            return True
        return False

# Testowanie
with IgnorujBledy((ValueError, TypeError)):
    int("abc")

print("Program działa dalej.")