class Ridic:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return f"Ridic: {self.jmeno}"

class Motor:
    def __init__(self, vykon):
        self.vykon = vykon
        self.__nastartovano = False
    
    def start(self):
        self.__nastartovano = True
    
    def __str__(self):
        return f"Motor o vykonu {self.vykon} {"je" if self.__nastartovano else "neni"} nastartovan"

class Car:
    def __init__(self, ridic):
        self.ridic = ridic
        self.motor = Motor("100kW")
    
    def __str__(self):
        return f"Auto s motorem: {self.motor} ridi {self.ridic}"


if __name__ == "__main__":
    ridic = Ridic("Karel")
    auto = Car(ridic)
    print(auto.motor)
    print(auto.ridic)
    del auto
    print(ridic)