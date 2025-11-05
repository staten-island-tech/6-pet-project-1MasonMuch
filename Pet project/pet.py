class pet:
    name = input("Input Your pet's name")
    age = 1
    happiness = 40

    def _init_(self, name, age, happiness):
        self.name = name
        self.age = age 
        self.happiness = happiness

    def play(self):
        