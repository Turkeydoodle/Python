print("Welcome to Woodworks!")
class Shop:
    def __init__(self, name):
        self.name =  name
    inventory = {
        "Table": 100,
        "Chair": 50,
        "Sofa": 20,
        "Children's Toy": 20   }
    def greet_customer(self):
        print(f"Welcome to {self.name}!")
    def display_inventory(self):        
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")
    def purchase_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
                print(f"You have purchased {quantity} {item_name}(s).")
            else:
                print(f"Sorry, we only have {self.inventory[item_name]} {item_name}(s) left.")
        else:
            print(f"Sorry, we do not have {item_name} in our inventory.")
    def chargecustomer(self, item_name, quantity):
        prices = {
            "Table": 200,
            "Chair": 100,
            "Sofa": 500,
            "Children's Toy": 30
        }
        if item_name in prices:
            total_cost = prices[item_name] * quantity
            print(f"The total cost for {quantity} {item_name}(s) is ${total_cost}.")
        else:
            print(f"Sorry, we do not have a price for {item_name}.")
input_item = ""
input_quantity = 0
def main():
    global input_item, input_quantity
    store= Shop("Woodworks")
    store.greet_customer()
    while True:
        userinput = input("What would you like to do? (1: View Inventory, 2: Purchase Item, 3: Pay) ")
        if userinput == "1":
            store.display_inventory()
        elif userinput == "2":
            input_item = input("What item would you like to purchase? (Table, Chair, Sofa, Children's Toy) ")
            input_quantity = int(input("How many would you like to purchase? "))
            store.purchase_item(input_item, input_quantity)
            store.chargecustomer(input_item, input_quantity)
        elif userinput == "3":
            charge = input("Would you like to pay now? (yes/no) ")
            if charge.lower() == "yes":
                store.chargecustomer(input_item, input_quantity)
                print("Thank you for shopping with us!")
                break
            else:
                print("You can pay later at the checkout.")
if __name__ == "__main__":    
    main()