
from os.path import exists

def keyboardInput(datatype,caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False   
    return value
filename = "fruits.txt"

def doMenu(filename):
    choice = -1
    while choice != 0:
        print("-------------------")
        print("|  0 - Exit       |")
        print("|  1 - List       |")
        print("|  2 - Add        |")
        print("|  3 - Edit       |")
        print("|  4 - Delete     |")
        print("-------------------")
        choice = keyboardInput(int, "Enter your choice: ", "Invalid choice")
        if choice==0:
            print("Zai Jian")
        elif choice == 1:
            printProduct(filename)
        elif choice == 2:
            addProduct(filename)
        elif choice == 3:
            editProduct(filename)
        elif choice == 4:
            deleteProduct(filename)

def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename,'xt')
        except Exception as e:
            print("Something went wrong when we create the file",e)
        else:
            createTitle(filename)
        finally:
            # filehandler is object
            # has may method like read, write and close
            filehandler.close()

# content = input("Fruit Name: ")
# filehandler = open(filename,'')

# open file using different syntax
#whenever we come out from this block,
# the resource will closed automatically
def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            # here | (pipe) is used as delimiter
            # we can use delimiter to split the line into
            # different columns
            filehandler.write("Product|Quantity|Price")
    except Exception as e:
        print("Something went wrong when we write to the file", e)

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be integer")
        price = keyboardInput(float, "Price: ", "Price must be float")

        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we write to the file", e)

def printProduct(filename):
    lines = None
    try:
        with open(filename, 'rt') as filehandler:
            lines = filehandler.readlines()
        for index,line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            
            if(index == 0):
                print(f"{"No:":5}{product:40}{quantity:>20}{price:>20}")
                print("=" * 85)
            else:
                print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e:
        print("Something went wrong when we read from the file", e)

def editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        print(data)

        index = keyboardInput(int,"Plesase insert line number", "Number must be integer")
        if index >= 4:
            print("You can't edit this line")
        else:
            product, quantity, price = data[index]
            print(f"{product}, {quantity}, {price}")
            confirm = keyboardInput(str, "Are you sure?  (y/n): ", "Please insert y or n")
            if confirm == "y":
                newproduct = keyboardInput(str, f"Product[{product}]: ", f"Product must be string", product)
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", f"Quantity must integer", quantity)
                newprice = keyboardInput(float, f"Price[{price}]: ", f"Price must float", price)
                data[index] = [newproduct, newquantity, newprice]

                newlines = []
                for prod in data:
                    line = "|".join(map(str,prod)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)

    except Exception as e:
        print("Error edit product:", e)

def deleteProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        print(data)

        index = keyboardInput(int,"Plesase insert line number", "Number must be integer")
        if index >= 4:
            print("You can't edit this line")
        else:
            product, quantity, price = data[index]
            print(f"{product}, {quantity}, {price}")
            confirm = keyboardInput(str, "Are you sure?  (y/n): ", "Please insert y or n")
            if confirm == "y":
                del data[index]
                newlines = []
                for prod in data:
                    line = "|".join(map(str,prod)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)

    except Exception as e:
        print("Error edit product:", e)

filename = 'fruits.txt'
createFile(filename)
doMenu(filename)
# addProduct(filename)
# printProduct(filename)