class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Stimulates a dog sitting in response to a command"""
        print(f"{self.name} is now sitting down")

    def roll_over(self):
        """Stimulates a dog rolling over on a command"""
        print(f"{self.name} rolled over")


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
Dog.roll_over(my_dog)
Dog.sit(my_dog)
my_dog.sit()
my_dog.roll_over()
#           CREATING multiple instances
your_dog = Dog('Lucy', 3)
your_dog.sit()
print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
