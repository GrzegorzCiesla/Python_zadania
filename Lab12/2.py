import pickle


class StanGry:
    def __init__(self, nazwa_gracza, punkty, ekwipunek):
        self.nazwa_gracza = nazwa_gracza
        self.punkty = punkty
        self.ekwipunek = ekwipunek

    def __repr__(self):
        return f"StanGry(gracz='{self.nazwa_gracza}', pkt={self.punkty}, eq={self.ekwipunek})"


stan = StanGry("Wiedźmin", 100, ["Miecz", "Mikstura"])

with open("stan_gry.pkl", "wb") as f:
    pickle.dump(stan, f)

with open("stan_gry.pkl", "rb") as f:
    wczytany_stan = pickle.load(f)

print(wczytany_stan)
print(type(wczytany_stan))