class Plebian:
    def _init_(self, name, money, inventory, pet):
        self.name = name
        self.money = money
        self.inventory = inventory

        def buy(self, item):
            self.inventory.append(item)
            print(self.inventory)


Xiyang = Plebian("Xiyang", 1, ["potion"])

Xiyang.buy ({"title": "sword", "atk": 34})
print(Xiyang._dict_)



class pouch:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 


    def deposit(self, amount):
        self.__balance += amount 

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
