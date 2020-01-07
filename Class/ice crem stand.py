from Restaurant2 import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavours, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
        self.cuisine_type = cuisine_type

    def flavour_list(self):
        flav = ""
        for i in self.flavours:
            flav = flav + i + " "
        print(f"This ice cream stand has the following flavours: {flav}")

    def describe_restaurant(self):
        print(f"The name of my ice cream stand is {self.restaurant_name}")


listflav = ["Vanilla", "Chocolate", "Orange"]
KwalityWalls = IceCreamStand("kwality walls", listflav)
print(KwalityWalls.cuisine_type)
KwalityWalls.flavour_list()
KwalityWalls.describe_restaurant()
print(KwalityWalls.cuisine_type)
