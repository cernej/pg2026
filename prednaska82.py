from abc import ABC, abstractmethod

class Zvire(ABC):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Zvire {self.name} dela {self.zvuk()}"
    
    @abstractmethod
    def zvuk(self):
        pass

class Pes(Zvire):
    def zvuk(self):
        return "haf"

class Kocka(Zvire):
    def zvuk(self):
        return "mnau"


if __name__ == "__main__":
    x = Pes("Alik")
    print(x)
    y = Kocka("Micina")
    print(y)