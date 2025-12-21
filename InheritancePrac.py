class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def start_engine(self):
        print(f"{self.brand} {self.model} is starting")


    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year released: {self.year}")
        


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        
    
    def open_trunk(self):
        print(f"Opening the trunk of {self.brand} {self.model}.")



class ElectricCar(Car):
    def __init__(self, brand, model, year, num_doors, battery_capacity):
        super().__init__(brand, model, year, num_doors)
        self.battery_capacity = battery_capacity


    def charge_battery(self):
        print(f"Charging the battery of {self.brand} {self.model}")



class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type


    def do_wheelie(self):
        print(f"{self.brand} {self.model} is doing a wheelie!")




car1 = Car("Lamborghini", "Sesto Elemento", 2000, 2)
bike1 = Motorcycle("Royal Enfield", "Model 1", 2000, "Cruiser")
eCar1 = ElectricCar("Tesla", "Model S", 2024, 4, 70000)

car1.start_engine()
car1.display_info()

bike1.start_engine()
bike1.display_info()

car1.open_trunk()
bike1.do_wheelie()
eCar1.charge_battery()

