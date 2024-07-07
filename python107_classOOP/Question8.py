
'''
Write a Python class Inventory with attributes like id, productName, 
availableQuantity and price. Add methods like addItem, updateItem, and checkItem_details.
Use a dictionary to store the item details, where the key is the id and the value 
is a dictionary containing the productName, availableQuantity and price.

Sample Data:
{
  "97410": {
    "name": "Television",
    "availableQuantity": 20,
    "price": 1455.99
  },
  "97411": {
    "name": "Radio",
    "availableQuantity": 32,
    "price": 654.25
  }
}

'''
class Inventory:
    def __init__(self):
        self.data = {
            "97410": {
                "name": "Television",
                "availableQuantity": 20,
                "price": 1455.99
            },
            "97411": {
                "name": "Radio",
                "availableQuantity": 32,
                "price": 654.25
            }
        }

    def checkItem(self, id):
        if id in self.data:
            return self.data[id]
        else:
            return "Item not found"

    def addItem(self, id, name, availableQuantity, price):
        if id in self.data:
            return "Item already exists"
        else:
            self.data[id] = {
                "name": name,
                "availableQuantity": availableQuantity,
                "price": price
            }
            return "Item added to inventory list"

    def updateItem(self, id, name, availableQuantity, price):
        if id in self.data:
            self.data[id] = {
                "name": name,
                "availableQuantity": availableQuantity,
                "price": price
            }
            return "Item updated in inventory list"
        else:
            return "Item not found"

    def inventoryList(self):
        print("\nInventory list: ")
        for items in self.data:
            print(items, self.data[items])
        print("")


def main():
    item1 = Inventory()

    while True:
        print("     Main Menu          ")
        print("------------------------")
        print("|  0 - Exit            |")
        print("|  1 - Check Item      |")
        print("|  2 - Add Item        |")
        print("|  3 - Update Item     |")
        print("|  4 - Inventory List  |")
        print("------------------------")
        choice = int(input("Enter choice number: "))

        if choice == 0:
            print("Thank You!")
            break
        elif choice == 4:
            item1.inventoryList()
        elif choice == 1 or choice == 2 or choice == 3:
            id = input("Enter Item ID: ")
            if choice == 1:
                print(item1.checkItem(id))
            else:
                if choice == 2:
                    if id in item1.data:
                        print("Item already exists")
                    else:
                        name = input("Enter Item Name: ")
                        availableQuantity = int(input("Enter Item Available Quantity: "))
                        price = float(input("Enter Item Price: "))
                        print(item1.addItem(id, name, availableQuantity, price))

                elif choice == 3:
                    if id in item1.data:
                        name = input("Enter Item Name: ")
                        availableQuantity = int(input("Enter Item Available Quantity: "))
                        price = float(input("Enter Item Price: "))
                        print(item1.updateItem(id, name, availableQuantity, price))
                    else:
                        print("Item not found")
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()