import re
from datetime import datetime


def analizuj_czas_logow(sciezka_pliku):
    with open(sciezka_pliku, 'r') as f:
        tekst = f.read()

    wzorzec_daty = r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
    daty_str = re.findall(wzorzec_daty, tekst)

    format_daty = '%d/%b/%Y:%H:%M:%S'
    daty_obj = [datetime.strptime(d, format_daty) for d in daty_str]

    if not daty_obj:
        return None

    min_czas = min(daty_obj)
    max_czas = max(daty_obj)

    return max_czas - min_czas


# Testowanie (na pliku z Zadania 1)
roznica = analizuj_czas_logow("log.txt")
print(f"Różnica czasu: {roznica}")