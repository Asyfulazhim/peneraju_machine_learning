from os.path import exists
import _mysql_connector as mysql

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
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "peneraju"
    )
    return connection

def printProduct(connection):
    SQL = f"SELECT id, name, description, quantity, price FROM produts"
    cursor = connection.cursor()
    cursor.execute(SQL)
    print(f"{'Id':6s}|{'Name':20s}|{'Description':40s}|{'Quantity':20s}|{'Price':20s}")
    print("="*120)
    for id, name, description, quantity, price in cursor:
        print(f"{id:6s}|{name:20s}|{description:40s}|{quantity:20s}|{price:20s}")
    

connection = dbConnect
doMenu(connection)