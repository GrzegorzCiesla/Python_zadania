import re

def parsuj_logi(sciezka_pliku):
    try:
        with open(sciezka_pliku, 'r') as plik:
            tekst = plik.read()

        adresy_ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", tekst)
        kody_statusu = re.findall(r'" (\d{3})', tekst)

        return {'adresy_ip': adresy_ip, 'kody_statusu': kody_statusu}
    except FileNotFoundError:
        return {}

# Przygotowanie pliku log.txt
log_content = """127.0.0.1 - - [28/Oct/2023:10:55:36] "GET /index.html" 200
89.161.25.13 - - [28/Oct/2023:10:56:01] "POST /login" 404
212.77.100.101 - - [28/Oct/2023:10:57:15] "GET /admin" 500
127.0.0.1 - - [28/Oct/2023:10:58:00] "GET /dashboard" 200"""

with open("log.txt", "w") as f:
    f.write(log_content)

wynik = parsuj_logi("log.txt")
print(wynik)