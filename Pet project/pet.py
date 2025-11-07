
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

import random



name = input("Input a name for yor pet")
age = 1
happiness = 50
status = "alive"
pet1 = pet(name, age, happiness)
action = ""
randomnumber = 0
print(f"pet name: {name} pet age: {age} happiness: {happiness} status: {status}")


while status == "alive":
    action = input("Type 'ok' to play with pet")

    
    
    randomnumber = random.randint(1,2)
    print(randomnumber)
    if randomnumber == 2:
        happiness = happiness - 10
        
    if happiness == 0 or happiness < 0:
        status = "dead"
        print("Your pet had died! game over")