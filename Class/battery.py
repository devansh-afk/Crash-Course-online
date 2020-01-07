from car import Car


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialises the battery's attributes"""
        self.battery_size = battery_size
        self.range = 0

    def describe_battery(self,):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            self.range = 260
        elif self.battery_size == 100:
            self.range = 315
        print(f"This car can go about {self.range} miles on a full charge")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.Battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.Battery.describe_battery()} kWh battery")

    def fill_gas_tank(self):
        print("This car tank does not need a gas tank!")


My_Tesla = ElectricCar('Tesla', 'Model S', 2019)
print(My_Tesla.get_descriptive_name())
print(My_Tesla.describe_battery())
print(My_Tesla.Battery.battery_size)
My_Tesla.Battery.get_range()
