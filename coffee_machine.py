class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    status = "standby"

    def buy(self):
        coffee_type = input("What do you want to buy?  1 - espresso, 2 - latte, 3 - cappuccino")
        if coffee_type == "1":
            if self.water >= 250:
                if self.beans >= 16:
                    if self.cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 250
                        self.beans -= 16
                        self.cups -= 1
                        self.money += 4
                    else:
                        print("Sorry, not enough cups!")
                else:
                    print("Sorry, not enough beans!")
            else:
                print("Sorry, not enough water!")

        elif coffee_type == "2":
            if self.water >= 350:
                if self.milk >= 75:
                    if self.beans >= 20:
                        if self.cups >= 1:
                            print("I have enough resources, making you a coffee!")
                            self.water -= 350
                            self.milk -= 75
                            self.beans -= 20
                            self.cups -= 1
                            self.money += 7
                        else:
                            print("Sorry, not enough cups!")
                    else:
                        print("Sorry, not enough beans!")
                else:
                    print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough water!")

        elif coffee_type == "3":
            if self.water >= 200:
                if self.milk >= 100:
                    if self.beans >= 12:
                        if self.cups >= 1:
                            print("I have enough resources, making you a coffee!")
                            self.water -= 200
                            self.milk -= 100
                            self.beans -= 12
                            self.cups -= 1
                            self.money += 6
                        else:
                            print("Sorry, not enough cups!")
                    else:
                        print("Sorry, not enough beans!")
                else:
                    print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough water!")
        else:
            print("""What do you want to buy? 
                                1 - espresso,
                                2 - latte,
                                3 - cappuccino""")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        water_fill = int(input())
        self.water += water_fill
        print("Write how many ml of milk do you want to add:")
        milk_fill = int(input())
        self.milk += milk_fill
        print("Write gow many grams of coffee beans do you want to add:")
        beans_fill = int(input())
        self.beans += beans_fill
        print("Write how many disposable cups of coffee do you want to add:")
        cups_fill = int(input())
        self.cups += cups_fill

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money -= self.money

    def remaining(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("${} of money".format(self.money))

    def action(self):
        print("Write action (buy, fill, take, remaining, exit):")
        self.status = input()
        if self.status == "remaining":
            self.remaining()
        elif self.status == "buy":
            self.buy()
        elif self.status == "fill":
            self.fill()
        elif self.status == "take":
            self.take()


machine = CoffeeMachine()
while machine.status != "exit":
    machine.action()
