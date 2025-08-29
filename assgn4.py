# Meet the Superheroes!

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"Hi! I'm {self.name}, and I watch over {self.city}.")

    def use_power(self):
        print(f"{self.name} uses their amazing power: {self.power}!")

# A superhero who can fly!
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed
    def use_power(self):
        print(f"{self.name} zooms through the clouds at {self.flight_speed} km/h, using {self.power}!")

# Let's meet some vehicles and see how they move!
