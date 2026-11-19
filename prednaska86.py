class ZapornyZustatek(Exception):
    pass

class BankovniUcet:
    def __init__(self):
        self.__zustatek = 0
    
    def get_zustatek(self):
        return self.__zustatek
    
    def set_zustatek(self, hodnota):
        if hodnota < 0:
            raise ZapornyZustatek("Nelze nastavit zaporny zustatek")
        self.__zustatek = hodnota


if __name__ == "__main__":

    u = BankovniUcet()
    print(u.get_zustatek())
    u.set_zustatek(100)
    print(u.get_zustatek())