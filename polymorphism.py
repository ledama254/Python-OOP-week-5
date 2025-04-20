# polymorphism.py

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Function to demonstrate polymorphism
def travel(vehicle):
    vehicle.move()

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    travel(v)
