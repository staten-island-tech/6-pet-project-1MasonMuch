
class pet():
    def __init__(self, name, happiness, age):
        self.name = name
        self.happiness = happiness
        self.age = age
    
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

import random



name = input("Input a name for your pet")
age = 1
happiness = 50
status = "alive"
pet1 = pet(name, happiness, age)
action = ""
randomnumber = 0
print(f"pet name: {name} pet age: {age} happiness: {happiness} status: {status}")


while status == "alive":
    action = input("Type 'yes' to procede")

    
    
    randomnumber = random.randint(1,2)
    print(randomnumber)
    if randomnumber == 2:
        pet1.happiness -= 10
        print("Your pet lost 10 happiness interact again.")
         
    if pet1.happiness <= 0:
        status = "dead"
        print("Your pet had died! game over")
        break 

    if randomnumber == 1:
        print("You played with pet!")
        pet1.play()

    pet1.get_older()




print(pet1.name, pet1.age, pet1.happiness, status)