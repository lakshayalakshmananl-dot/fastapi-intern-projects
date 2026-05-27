class Car:
    # 1. The __init__ method sets up the initial data
    # 2. 'self' makes sure the data sticks to the specific car being made
    def __init__(self, brand, color):
        self.brand = brand   # This is an instance variable (attribute)
        self.color = color   # This is another instance variable
        self.odometer = 0    # All cars start with 0 miles

    # 3. This is an Instance Method (an action the car can take)
    def drive(self, miles):
        self.odometer += miles
        print(f"The {self.color} {self.brand} drove {miles} miles.")
        print(f"Total mileage is now: {self.odometer} miles.\n")

# --- Using the Class to create Objects ---

# We create two distinct objects. 
# "Toyota" and "Blue" are passed directly to the __init__ method.
car_a = Car("Toyota", "Blue")
car_b = Car("Tesla", "Red")

# We call the instance methods on each specific object
car_a.drive(50)
car_b.drive(120)