
class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.start()
    
    def get_action(self):
        print("Write action (buy, fill, take, remaining, exit):")
        return input()
    
    def check_resources(self, needed_water=0, needed_milk=0, needed_coffee=0):
        if self.water < needed_water:
            print("Sorry, not enough water!")
            return False
        if self.milk < needed_milk:
            print("Sorry, not enough milk!")
            return False
        if self.coffee < needed_coffee:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups == 0:
            print("Sorry, not enough disposable cups!")
            return False
        return True
    
    def is_enough(self, needed_water=0, needed_milk=0, needed_coffee=0):
        if not self.check_resources(needed_water, needed_milk, needed_coffee):
            return False
        print("I have enough resources, making you a coffee!")
        return True
    
    def make_coffee(self, u_water=0, u_milk=0, u_coffee=0, a_money=0):
        
        self.water -= u_water
        self.milk -= u_milk
        self.coffee -= u_coffee
        self.cups -= 1
        self.money += a_money
    
    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        type_of_coffee = input()
        if type_of_coffee == "back":
            return 1
        elif int(type_of_coffee) == 1 and self.is_enough(needed_water=250, needed_coffee=16):
            self.make_coffee(u_water=250, u_coffee=16, a_money=4)
        elif int(type_of_coffee) == 2 and self.is_enough(350, 75, 20):
            self.make_coffee(u_water=350, u_milk=75, u_coffee=20, a_money=7)
        elif int(type_of_coffee) == 3 and self.is_enough(200, 100, 12):
            self.make_coffee(u_water=200, u_milk=100, u_coffee=12, a_money=6)

        
    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        
    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        
    def print_status(self):
        print()
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")
        print()
            
       
    def start(self):
        while True:
            action = self.get_action()
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.print_status()
            else:
                break
                
cf = CoffeeMachine()
