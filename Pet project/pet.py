
import random

class pet():
    def __init__(self, name, happiness, age, hunger, hp, xp, lvl):
        self.name = name
        self.happiness = happiness
        self.age = age
        self.hunger = hunger
        self.hp = hp
        self.xp = xp
        self.lvl = lvl


    def get_older(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")
    
    def play(self):
        if self.happiness == 100:
            print("Your pet is too excited")
        elif self.happiness > 100:
            print("Your pet is too excited")
        else:
            self.happiness += 10
            print(f" You played with {self.name} and its happiness is now a {self.happiness}")

    def eat(self):
        number = random.randint(1,10)
        if number == 2 or number == 4 or number == 8:
            self.hp = self.hp - 10
            print("Your pet got food poisoning and lost and lost 10 hp")
        else:
            fullness = fullness + 10
            print("Your pet ate and gained 10 fullness")
            if fullness >= 90 and fullness <= 100:
                self.hunger = "Very Full"
            if fullness >= 70 and fullness < 90:
                self.hunger = "Full"




name = input("Input a name for your pet")
age = 1
happiness = 50
status = "alive"
pet1 = pet(name, happiness, age)
action = ""
randomnumber = 0



