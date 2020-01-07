"""A class that represents a Restaurant"""


class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of my restaurant is {self.restaurant_name}")
        print(f"The cuisine type of my restaurant is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment_num):
        self.number_served += increment_num

    def return_number_served(self):
        print(f"{self.restaurant_name} has served {self.number_served} customers")
