class Users:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"The name of the user is {self.first_name} {self.last_name}")
        print(f"{self.first_name} is {self.age} years old and is a {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name}. Hope you are having a great and marvellous day")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


Devansh = Users('Devansh', 'Bansal', 16, 'Male')
Devansh.increment_login_attempts()
Devansh.increment_login_attempts()
Devansh.increment_login_attempts()
print(Devansh.login_attempts)
Devansh.reset_login_attempts()
print(Devansh.login_attempts)
