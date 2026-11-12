class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
    
    def __str__(self):
        return f'Osoba {self.jmeno} ma {self.vek} let'

    def pridat_rok(self):
        self.vek += 1



if __name__ == "__main__":
    osoba = Osoba("Vlada", 44)
    
