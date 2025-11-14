
import random


class pet():
    def __init__(self, name, happiness, age, hunger, hp, fullness):
        self.name = name
        self.happiness = happiness
        self.age = age
        self.hunger = hunger
        self.hp = hp
        self.fullness = fullness


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
            self.fullness = self.fullness - 20
            print(f" You played with {self.name} and its happiness is now a {self.happiness}")

    def eat(self):
        number = random.randint(1,10)
        if number == 2 or number == 4 or number == 8:
            self.hp = self.hp - 10
            print("Your pet got food poisoning and lost and lost 10 hp")
        else:
            fullness = fullness + 10
            print("Your pet ate and gained 10 fullness")
            if self.fullness >= 90 and fullness <= 100:
                self.hunger = "Very Full"
            if self.fullness >= 70 and fullness < 90:
                self.hunger = "Full"
            if self.fullness >= 40 and fullness <=69:
                self.hunger = "Hungry"
            if self.fullness > 0 and fullness <= 39:
                self.hunger = "Starving"
            print(self.hunger)

    def health(self):
        
        if self.fullness <= 0:
            self.hp - 30
        print(f"Your pet is {self.hunger} and lost 30hp your hp is now {self.hp}.")
        if self.happiness <= 50:
            self.hp - 10
            print(f"Your pet is depressed and lost 10hp your hp is now {self.hp}.")
        if self.fullness >= 90 and fullness <= 100:
            self.hunger = "Very Full"
        if self.fullness >= 70 and fullness < 90:
            self.hunger = "Full"
        if self.fullness >= 40 and fullness <=69:
            self.hunger = "Hungry"
        if self.fullness > 0 and fullness <= 39:
            self.hunger = "Starving"
        print(self.hunger)
        if self.hp <= 0:
            status = "dead"

            print(f"Your pet is {status}.")




name = input("Input a name for your pet")
age = 1
happiness = 50
status = "alive"
hunger = "Full"
fullness = 80
hp = 100
pet1 = pet(name, happiness, age, hunger, hp, fullness)
action = ""

while status == "alive":
    action = input("Options:eat or play")
    if action == "Eat" or action == "eat":
        pet1.eat()
        pet1.health
    if action == "Play" or action == "play":
        pet1.play
        pet1.health