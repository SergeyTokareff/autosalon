class Car:
    def __init__(self, model: str, year: int, color: str, speed: int, doors: int ):
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed
        self.doors = doors

    def print_info(self):
        print(f"Model: {self.model}, Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h, Doors: {self.doors}")

class AutoSalon:
    def __init__(self):
        self.list_cars = []

    def show_available_cars(self):
        for car in self.list_cars:
            car.print_info()

    def sell_car(self, model: str):
        for car in self.list_cars:
            if car.model == model:
                self.list_cars.remove(car)
                print(f"Автомобіль {car.model} був проданий.")
                return

salon = AutoSalon()

salon.list_cars.append(Car(model='BMW X6', year=2022, color='black', speed=240, doors=5))
salon.list_cars.append(Car(model='Audi Q7', year=2020, color='white', speed=220, doors=5))
salon.list_cars.append(Car(model='Hyundai Sonata', year=2018, color='grey', speed=180, doors=4))
salon.list_cars.append(Car(model='Lexus RX 350', year=2022, color='green', speed=240, doors=5))
salon.list_cars.append(Car(model='Porsche 911', year=2023, color='yellow', speed=280, doors=3))

salon.show_available_cars()

salon.sell_car('Audi Q7')
salon.sell_car('BMW X6')

salon.show_available_cars()