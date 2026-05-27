class Vehicle():

    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def start_engine(self):
        print("The engine is starting...")

class Car(Vehicle):

    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    # перевизначаємо метод батьківського класу
    def start_engine(self):
        print("The car's engine is starting...")

    def drive(self):
        print(self.make + " " + self.model + " поїхав!")

class Truck(Vehicle):

    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def start_engine(self):
        print("The truck's engine is starting...")

    def haul(self):
        print(self.make + " " + self.model + " везе вантаж " + str(self.cargo_capacity) + " кг")

class Motorcycle(Vehicle):

    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def start_engine(self):
        print("The motorcycle's engine is starting...")

    def ride(self):
        print(self.make + " " + self.model + " поїхав на колесах: " + str(self.num_wheels))

my_car = Car("Toyota", "Camry", 2020, 1500, 4, 5)
my_truck = Truck("Ford", "F-150", 2019, 3000, 1000, 5000)
my_moto = Motorcycle("Honda", "CBR", 2021, 200, 2, False)

print("--- Легковик ---")
my_car.start_engine()
my_car.drive()

print()
print("--- Вантажівка ---")
my_truck.start_engine()
my_truck.haul()

print()
print("--- Мотоцикл ---")
my_moto.start_engine()
my_moto.ride()

print()
print("--- Поліморфізм ---")

all_vehicles = [my_car, my_truck, my_moto]

for vehicle in all_vehicles:
    vehicle.start_engine()