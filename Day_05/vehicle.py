class Vehicle:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self._speed = speed   # protected attribute

    def accelerate(self, amount):
        self._speed += amount
        print(f"Accelerated! Speed is now {self._speed} km/h")

    def brake(self, amount):
        self._speed -= amount

        if self._speed < 0:
            self._speed = 0

        print(f"Braked! Speed is now {self._speed} km/h")

    def get_info(self):
        return f"{self.make} {self.model} traveling at {self._speed} km/h"


class Car(Vehicle):
    def __init__(self, make, model, speed, num_doors):
        super().__init__(make, model, speed)
        self.num_doors = num_doors

    # Method overriding
    def get_info(self):
        return (
            f"Car: {self.make} {self.model}, "
            f"Speed: {self._speed} km/h, "
            f"Doors: {self.num_doors}"
        )


class Truck(Vehicle):
    def __init__(self, make, model, speed, payload_capacity):
        super().__init__(make, model, speed)
        self.payload_capacity = payload_capacity

    # Method overriding
    def get_info(self):
        return (
            f"Truck: {self.make} {self.model}, "
            f"Speed: {self._speed} km/h, "
            f"Payload Capacity: {self.payload_capacity} tons"
        )


# Testing
car1 = Car("Toyota", "Corolla", 80, 4)
truck1 = Truck("Volvo", "FH16", 60, 25)

print(car1.get_info())
print(truck1.get_info())

car1.accelerate(20)
truck1.brake(10)
