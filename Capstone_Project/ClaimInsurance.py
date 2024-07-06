def keyboardInput(datatype, caption, errorMessage):
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

def doMenu (filename):
    choice = -1
    while choice != 0:
        print("---------------------------------")
        print("|  0 - Exit                     |")
        print("|  1 - Create Car Insurance     |")
        print("|  2 - Create Driver Insurance  |")
        print("|  3 - Claim Insurance          |")
        print("|  4 - Print Resit              |")
        print("---------------------------------")
        choice = keyboardInput(int, "Enter your choice: ", "Invalid choice")
        if choice==0:
            print("Zai Jian")
        elif choice == 3:
            readCarFile(filename)
            chooseBookingID()
        # elif choice == 2:
        #     addProduct(filename)
        # elif choice == 3:
        #     editProduct(filename)
        # elif choice == 4:
        #     deleteProduct(filename)

def readCarFile(carfile):
    with open (carfile, "r") as file:
        cars = file.read()
        print (cars)



carfile = "Car.txt"
driverfile = "Driver.txt"
doMenu(carfile)