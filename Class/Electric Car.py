from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size} kWh battery")

    def fill_gas_tank(self):
        print("This car tank does not need a gas tank!")


my_tesla = ElectricCar('Tesla', 'Model S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
