class Ucet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0

    def vklad(self, castka):
        if castka <= 0:
            print(f"Nemuzu vlozit castku {castka} kc")
            return
        self.__zustatek += castka

    def vyber(self, castka):
        if castka <= 0:
            print(f"Nemuzu vybrat castku {castka} kc")
            return
        if castka > self.__zustatek:
            print(f"Nemuzu vybrat {castka} kc, protoze na ucte je {self.__zustatek} kc")
            return
        self.__zustatek -= castka

    def popis(self):
        print(f"Na ucte {self.jmeno} je {self.__zustatek} kc")


if __name__ == "__main__":

    bezny_ucet = Ucet("Nas bezny ucet")

    bezny_ucet.vklad(100)
    bezny_ucet.vyber(50)
    bezny_ucet.vyber(50)
    bezny_ucet.vyber(50)

    bezny_ucet.popis()