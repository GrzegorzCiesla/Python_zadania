from pathlib import Path
import datetime

folder_glowny = Path("raporty_dzienne")
data_dzis = datetime.date.today()
folder_data = data_dzis.strftime("%Y-%m-%d")
sciezka_pliku = folder_glowny / folder_data / "raport.txt"

sciezka_pliku.parent.mkdir(parents=True, exist_ok=True)
sciezka_pliku.write_text("To jest treść raportu.", encoding="utf-8")

tresc = sciezka_pliku.read_text(encoding="utf-8")
print(tresc)

print(sciezka_pliku.resolve())
print(sciezka_pliku.name)
print(sciezka_pliku.parent)