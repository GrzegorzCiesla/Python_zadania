def przygotuj_pizze(dodatki, baza=None):
    if baza is None:
        baza = []
    baza.append("sos pomidorowy")
    baza.append("ser")
    baza.extend(dodatki)
    print(f"Pizza gotowa! Składniki: {baza}")

print("--- Zamówienie 1: Capricciosa ---")
przygotuj_pizze(["szynka", "pieczarki"])

print("\n--- Zamówienie 2: Margherita ---")
przygotuj_pizze([])