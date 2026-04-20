
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
    def __init__(self,name,happiness,hunger):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
    def names(self):
        print("The cats name is Kon, he is happy to meet you!")
    def food(self):
        print("kon is much less hungry now!")
    def happinesses(self):
        print("The cat feels much better after a pet.")


Kon = pet("Kon",0,100)
print("Meet the orange cat!")  
con = True
hunger = 100
happiness = 0
while con == True:
    action = (input("What do you want to do with orange? [Pet, Feed or Talk]:  "))
    if action == "Pet":
        happiness += 20
        print("The cat feels much better after a pet :3")
    elif action == "Feed":
        print("kon is much less hungry now! :D")
        hunger -= 10
    elif action == "Talk":
        print("Meow, meow meow meow meow! (The cats name is Kon, he is happy to meet you!)")
        hunger += 5
        happiness += 5
    else:
        print("Please select one of the three options above.")
        
    Cont = (input("Do you want to continue interacting with Kon? [Yes or No]:  "))
    if Cont == "Yes":
        con = True
    else:
        break

print(f"Kons hunger level is", [hunger])
print(f"Kons happiness level is",[happiness])
print("Thank you for interacting with Kon! Meow :3")





    





   
   
   
   
   
   
   
   
   
   
   
   
   
   

   
   
"""     interaction = True
    while interaction == True:
        action = (input("What do you want to do with mr orange?  "))
        def hunger(self):
        if action == "Feed":
            print("You fed Kon! You decreased his hunger by 40!")
            self.hunger += 20
            def happiness(self):
                happi = 0 
        elif action == "Pet":
                print("You petted Kon! He is now very happy! +30 happiness.")
                happi += 30
                def play(self):
        elif action == "Play":
                print("You played with Kon! He is now more playful! +25 fun")
                plays += 25
                question = (input("Do you still want to interact with Kon?   "))
                if question == "Yes":
                    interaction = True
                elif question == "No":
                    interaction = False """

    





