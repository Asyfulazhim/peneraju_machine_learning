from os.path import exists
import mysql.connector as mysql

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

def doMenu(connection):
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
            printProduct(connection)
        elif choice == 2:
            addProduct(connection)
        elif choice == 3:
            editProduct(connection)
        elif choice == 4:
            deleteProduct(connection)

def dbConnect():
    connection = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database = "peneraju"
    )
    return connection

def printProduct(connection):
    SQL = f"SELECT id, name, description, quantity, price FROM products"
    cursor = connection.cursor()
    cursor.execute(SQL)
    print(f"{'Id':6s}|{'Name':20s}|{'Description':40s}|{'Quantity':20s}|{'Price':20s}")
    print("="*120)
    for id, name, description, quantity, price in cursor:
        print(f"{id:6d}|{name:20s}|{description:40s}|{quantity:20d}|{price:20f}")
    print("="*120)
    
def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        description = keyboardInput(str, "Description: ", "Description must be String")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be integer")
        price = keyboardInput(float, "Price: ", "Price must be float")
        SQL = f"INSERT INTO products (name, description, quantity, price) VALUES ('{product}', '{description}',{quantity}, {price} )"
        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit()

        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we write to the file", e)

def editProduct(connection):
    try:
        id = keyboardInput(int,"Plesase insert line number", "Number must be integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()

    except:
        print("Product for this id does not exists") 

    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\nPrice: {price}")
        
        confirm = keyboardInput(str, "Are you sure?  (y/n): ", "Please insert y or n")
        if confirm == "y":
            newproduct = keyboardInput(str, f"Product[{name}]: ", f"Product must be string", name)
            newdescription = keyboardInput(str, f"Description[{description}]: ", f"Description must integer", description)
            newquantity = keyboardInput(float, f"Quantity[{quantity}]: ", f"Quantity must float", quantity)
            newprice = keyboardInput(float, f"Price[{price}]: ", f"Price must float", price)
            SQL = f"""UPDATE products SET name = '{newproduct}', description = '{newdescription}', quantity= {newquantity}, price= {newprice} WHERE id = {id}"""

            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()

def deleteProduct(filename):
    try:
        id = keyboardInput(int,"Plesase insert line number", "Number must be integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()

    except:
        print("Product for this id does not exists") 

    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\nPrice: {price}")
        confirm = keyboardInput(str, "Are you sure?  (y/n): ", "Please insert y or n")
        if confirm == "y":
            SQL = f"DELETE FROM products WHERE id = {id}"
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()

connection = dbConnect()
doMenu(connection)