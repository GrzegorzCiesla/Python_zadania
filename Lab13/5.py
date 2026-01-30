import threading
import time

dostepne_bilety = 5
blokada = threading.Lock()


def kup_bilet_bezpiecznie(klient_id):
    global dostepne_bilety

    with blokada:
        if dostepne_bilety > 0:
            time.sleep(0.1)
            dostepne_bilety -= 1
            print(f"Klient {klient_id} kupił bilet. Zostało: {dostepne_bilety}")
        else:
            print(f"Klient {klient_id} odszedł z kwitkiem.")


watki = []
for i in range(10):
    t = threading.Thread(target=kup_bilet_bezpiecznie, args=(i,))
    watki.append(t)

for t in watki:
    t.start()

for t in watki:
    t.join()

print(f"Końcowa liczba biletów: {dostepne_bilety}")