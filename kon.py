""" class pets:
    def __init__(self,name,hunger,happiness):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness

Kon = pets("Kon")

action = input("What do you want to do with Mr.Orange? Feed, play or say Hi. ")


def hunger(self):
    self.hunger = 0
    if action == "Feed":
        print("You fed the kitty cat!")
        self.hunger += 5

def happiness(self):
    self.happiness = 0
    if action == "Play":
        print("You made the Kon happy!")
        self.happiness += 5 """
                  
""" class Calculator():
    def add(x,y):
        print( x + y)
        return x + y
    def add_many(numbers):
        print(sum(numbers))
    def subtract(numbers):
        return numbers
Calculator.add(6,7) """
""" 
class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Kon = Hero("Kon",67,["Kibble, churu, toys"])
Kon.buy({"title": "Scratching post","happiness": 100})
print(Kon.__dict__) """

""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        print(f"{self.owner} has ${self._balance}") """

class pet:
    def _init_(self,name,happiness, hunger, play):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.play = play
        name = "Kon"

    interaction = True

    while interaction == True:
        action = (input("What do you want to do with mr orange?"))
    def hunger(self):
        hunger = 100
    if action == "Feed":
        print("You fed Kon! You decreased his hunger by 40!")
        hunger -= 40
    def happiness(self):
        happiness = 0 
    if action == "Pet":
        print("You petted Kon! He is now very happy! +30 happiness.")
        happiness += 30
    def play(self):
        play = 0
    if action == "Play":
        print("You played with Kon! He is now more playful! +25 fun")
        play += 25
    question = (input("Do you still want to interact with Kon?"))
    if question == "Yes":
        interaction = True
    elif question == "No":
        interaction = False

    





