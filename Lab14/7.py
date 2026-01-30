import itertools

# Przygotowanie pliku logs.txt
log_data = """1.2.3.4 - - [11/Nov/2023] "GET /" 200 150
5.6.7.8 - - [11/Nov/2023] "GET /admin" 401 100
1.2.3.4 - - [11/Nov/2023] "POST /login" 404 250
9.1.2.3 - - [11/Nov/2023] "GET /" 200 180
5.6.7.8 - - [11/Nov/2023] "GET /data.json" 200 950
1.2.3.4 - - [11/Nov/2023] "GET /static/img.jpg" 404 50
2.3.4.5 - - [11/Nov/2023] "GET /api/v1/users" 403 120"""

with open("logs.txt", "w") as f:
    f.write(log_data)

def czytaj_logi(sciezka):
    with open(sciezka, "r") as f:
        for line in f:
            yield line.strip()

# Potok przetwarzania
zrodlo = czytaj_logi("logs.txt")

# Filtr (status 4xx) - proste sprawdzenie czy " 4" występuje w odpowiednim miejscu
# lub splitowanie. Tutaj zakładamy prosty split.
parsowane = (line.split() for line in zrodlo)
bledy_4xx = (parts for parts in parsowane if int(parts[-2]) >= 400 and int(parts[-2]) < 500)

# Transformacja -> (ip, size)
dane_ip_size = ((parts[0], int(parts[-1])) for parts in bledy_4xx)

# Sortowanie po IP (dla groupby)
posortowane_ip = sorted(dane_ip_size, key=lambda x: x[0])

# Grupowanie i sumowanie
wyniki = []
for ip, grupa in itertools.groupby(posortowane_ip, key=lambda x: x[0]):
    suma_bajtow = sum(x[1] for x in grupa)
    wyniki.append((ip, suma_bajtow))

# Sortowanie końcowe (top 3 wg ruchu)
top_3 = sorted(wyniki, key=lambda x: x[1], reverse=True)[:3]

print(top_3)