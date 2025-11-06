
class pet():
    def __init__(self, name, happiness, age):
        self.name = name
        self.happiness = happiness
        self. age = age
    def get_older(self, name, age):
        age = age + 1
        print(f"{name} is {age} years old!")
    
    def play(self):
        if self.happiness == 100:
            print("Your pet is too excited")
        elif self.happiness > 100:
            print("Your pet is too excited")
        else:
            self.happiness += 10
            print(f" You played with {self.name} and its happiness is now a {self.happiness}")

name = input("Input a name for yor pet")
age = 1
happiness = 50