import json


class Car:
    
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f"Car: {self.brand} {self.model} is {self.color}"
    
    def __repr__(self):
        return f"Car({self.brand}, {self.model}, {self.color})"

    @classmethod
    def load_data(cls, data):
        if 'brand' not in data or 'model' not in data or 'color' not in data:
            return None
        return cls(data['brand'], data['model'], data['color'])


if __name__ == "__main__":

    cars = []

    with open("data.json", "r") as fp:
        data = json.loads(fp.read())
        for record in data:
            cars.append(Car.load_data(record))
    
    print(cars)
    
