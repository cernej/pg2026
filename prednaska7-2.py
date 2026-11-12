from math import pi

class Tvar:
    def __init__(self, nazev="Obcecny tvar"):
        self.nazev = nazev
    def vrat_nazev(self):
        return self.nazev
    def spocitej_obsah(self):
        return 0.0

class Ctverec(Tvar):
    def __init__(self, hrana):
        super().__init__("Ctverec")
        self.hrana = hrana
    def spocitej_obsah(self):
        return self.hrana * self.hrana

class Kruh(Tvar):
    def __init__(self, polomer):
        super().__init__("Kruh")
        self.polomer = polomer
    def spocitej_obsah(self):
        return pi * self.polomer * self.polomer


if __name__ == "__main__":

    celkovy_obsah = 0
    tvary = [Ctverec(10), Ctverec(1), Kruh(1), Ctverec(5), Kruh(5), Kruh(3)]

    for tvar in tvary:
        print(tvar.spocitej_obsah())
        celkovy_obsah += tvar.spocitej_obsah()

    print(f"Celkovy obsah tvaru je: {celkovy_obsah}")
    