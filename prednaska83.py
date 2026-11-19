class Osoba:
    def __init__(self, jmeno, vek, pohlavi):
        self.jmeno = jmeno
        self.vek = vek
        self.pohlavi = pohlavi

    def __str__(self):
        return f"Osoba {self.jmeno} ma {self.vek} let a je to {self.pohlavi}"
    
    def __eq__(self, other):
        return self.jmeno == other.jmeno and self.vek == other.vek and self.pohlavi == other.pohlavi


if __name__ == "__main__":
    o1 = Osoba("Tomas", 20, "muz")
    print(o1)
    o2 = Osoba("Tomas", 20, "muz")
    print(o2)
    print(o1 == o2)