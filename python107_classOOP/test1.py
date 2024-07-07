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
        return self.data.get(id)

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
        return self.data


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
        choice = int(input("What is your purpose?: "))

        if choice == 0:
            print("Thank You!")
            break
        elif choice == 4:
            print(item1.inventoryList())
        else:
            id = input("Enter Item ID: ")
            if choice == 1:
                print(item1.checkItem(id))
            else:
                name = input("Enter Item Name: ")
                availableQuantity = int(input("Enter Item Available Quantity: "))
                price = float(input("Enter Item Price: "))
                if choice == 2:
                    print(item1.addItem(id, name, availableQuantity, price))
                elif choice == 3:
                    print(item1.updateItem(id, name, availableQuantity, price))


if __name__ == "__main__":
    main()
