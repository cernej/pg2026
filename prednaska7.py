class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.motor_bezi = False
        self.pocet_nastartovani = 0

    def start_engine(self):
        if not self.motor_bezi:
            self.motor_bezi = True
            self.pocet_nastartovani += 1
            print(f"{self.brand} {self.model} started engine")

    def stop_engine(self):
        if self.motor_bezi:
            self.motor_bezi = False
            print(f"{self.brand} {self.model} stoped engine")

    def kolikrat_bylo_auto_nastartovano(self):
        print(f"{self.brand} {self.model} bylo nastartovano {self.pocet_nastartovani} krat")


if __name__ == "__main__":
    auto1 = Car("Toyota", "Corrola", "Blue")
    auto2 = Car("Ford", "Mustang", "Red")

    Car.start_engine(auto1)
    Car.stop_engine(auto1)

    auto2.start_engine()
    auto2.stop_engine()
    auto2.start_engine()
    auto2.stop_engine()
    auto2.start_engine()
    auto2.stop_engine()

    print(f"{auto1.brand} {auto1.model} ma {auto1.color} barvu")

    auto1.kolikrat_bylo_auto_nastartovano()
    auto2.kolikrat_bylo_auto_nastartovano()