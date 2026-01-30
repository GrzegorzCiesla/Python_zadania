def sprawdz_typy(typ_argumentu):
    def dekorator(funkcja):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, typ_argumentu):
                    print(f"Błąd: Argument {arg} nie jest typu {typ_argumentu}")
                    return None
            return funkcja(*args, **kwargs)
        return wrapper
    return dekorator

@sprawdz_typy(int)
def dodaj(a, b):
    return a + b

print(dodaj(10, 20))
print(dodaj(10, "20"))