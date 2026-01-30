import queue
import threading
import time

kolejka = queue.Queue()

def producent():
    for i in range(5):
        msg = f"Zgłoszenie nr {i}"
        kolejka.put(msg)
        print(f"Producent: dodano {msg}")
        time.sleep(0.5)

def konsument():
    while True:
        zadanie = kolejka.get()
        print(f"Konsument: przetwarzam {zadanie}...")
        time.sleep(1)
        kolejka.task_done()

# Uruchomienie
t_konsument = threading.Thread(target=konsument, daemon=True)
t_konsument.start()

t_producent = threading.Thread(target=producent)
t_producent.start()

t_producent.join()
kolejka.join()
print("Wszystkie zadania wykonane.")