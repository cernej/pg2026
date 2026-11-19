class TridaA:
    def vypis(self):
        return "neco"

    def vypocet(self):
        return "Vysledek je A"

class TridaB:
    def __init__(self):
        self.hodnota = 0

    def vypocet(self):
        return "Vysledek je B"

    def zapis(self, hodnota):
        self.hodnota = hodnota

class TridaC(TridaA, TridaB):
    def porovnej(self, a, b):
        return a == b


if __name__ == "__main__":

    c = TridaC()

    print(c.vypis())
    c.zapis(10)
    print(c.hodnota)

    print(c.vypocet())

