def generuj_raport(imie, stanowisko="Pracownik", miasto="Nieznane"):
    raport = "--- RAPORT PRACOWNIKA ---\n"
    raport += f"Imię: {imie}\n"
    raport += f"Stanowisko: {stanowisko}\n"
    raport += f"Miasto: {miasto}\n"
    raport += "-------------------------"
    return raport

gotowy_raport = generuj_raport("Marek", "Analityk", "Wrocław")
print(gotowy_raport)