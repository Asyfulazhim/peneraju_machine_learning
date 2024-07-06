import time

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

def doMenu (carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile):
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
            print("Thank You!!")
        elif choice == 1:
            createCarInsurance(carfile, carinsurancefile)
        elif choice == 2:
            createDriverInsurance(driverfile, driverinsurancefile)
        elif choice == 3:
            chooseBokingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile)            
        elif choice == 4:
            printResit(claiminsurancefile)

def readbookingfile(bookingfile):
    with open (bookingfile, "r") as file:
        booking = file.read()
        print (booking)

def createCarInsurance(carfile, carinsurancefile):
    pass
def createDriverInsurance(driverfile, driverinsurancefile):
    pass

def chooseBokingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile):
    with open(bookingfile, "rt") as file:
        display = file.read()
        print(display)
    try:
        lines = None
        with open(bookingfile, "rt") as file:
            lines = file.readlines()
            #print(lines)
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        #print(data)

        index = keyboardInput(int,"Plesase insert line number: ", "Number must be integer")
        BookingID, CustomerID, CarPlate, DriverID, DriverName, BookingDate = data[index]
        print(f"\nBooking ID: {BookingID}\nCustomer ID: {CustomerID}\nPlate No: {CarPlate}\nDriver ID: {DriverID}\nName: {DriverName}\nBooking Date: {BookingDate}")
        confirm = keyboardInput(str, "\nDetails is true?  (y/n): ", "Please insert y or n")
        if confirm == "y":
            print("\nDetail Claim Amont:")
            carClaim = findCarInsurance(carinsurancefile, CarPlate)
            driverClaim = findDriverInsurance(driverinsurancefile, DriverID)
            totalClaim = carClaim + driverClaim
            print(f"Total Claim: {totalClaim}")

            totalClaimInsurance(claiminsurancefile,BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim)
        #BookingID | CustomerID | CarPlate | DriverID | DriverName | BookingDate

    except Exception as e:
        print("Error edit product:", e)

def findCarInsurance (carinsurancefile,CarPlate):
    CarPlate = CarPlate.replace(" ","")
    #carinsurancefile = "CarInsurance.txt"
    with open(carinsurancefile, "rt") as file:
        lines = file.readlines()
    
    datas = []
    for line in lines:
        datas.append(line.strip().split(" | "))
    #print(data)
    for data in datas:
        #print(f"{data[0]}:")
        if data[0].replace(" ","") == CarPlate:
            print(f"Car Insurance Claim: {data[-1]}")
            break
            
    else:
        print("Car Insurance not found")
    
    return int(data[-1])

def findDriverInsurance (driverinsurancefile, DriverID):
    DriverID = DriverID.replace(" ","")
    # print(f"{DriverID}:")
    #driverinsurancefile = "DriverInsurance.txt"
    with open(driverinsurancefile, "rt") as file:
        lines = file.readlines()
    
    datas = []
    for line in lines:
        datas.append(line.strip().split(" | "))
    #print(data)
    for data in datas:
        # print(f"{data[0]}:")
        if data[0].replace(" ","") == DriverID:
            print(f"Driver Insurance Claim: {data[-1]}")
            break
    else:
        print("Driver Insurance not found")
    
    return int(data[-1])

def totalClaimInsurance (claimInsurancefile,BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim):
    #claimInsurancefile = "ClaimInsurance.txt"
    try:
        with open(claimInsurancefile, "at") as file:
            file.write(f"\n{BookingDate} | {CarPlate} | {carClaim} | {DriverID} | {driverClaim} | {totalClaim}")

    except Exception as e:
        print("Something went wrong when we write to the file", e)

def printResit (claimInsurancefile):
    lines = None
    #claimInsurancefile = "ClaimInsurance.txt"
    try:
        with open(claimInsurancefile, 'rt') as filehandler:
            lines = filehandler.readlines()
        for index,line in enumerate(lines):
            BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim = line.strip().split("|")
            
            if(index == 0):
                print(f"{"No:":5}{BookingDate:15}{CarPlate:>10}{carClaim:>22}{DriverID:>12}{driverClaim:>25}{totalClaim:>20}")
                print("=" * 110)
            else:
                CarPlate = CarPlate.strip()
                print(f"{index:<5}{BookingDate:15}{CarPlate:>10}{carClaim:>22}{DriverID:>12}{driverClaim:>25}{totalClaim:>20}")
        time.sleep(2)
    except Exception as e:
        print("Something went wrong when we read from the file", e)

carfile = "Car.txt"
driverfile = "Driver.txt"
carinsurancefile = "CarInsurance.txt"
driverinsurancefile = "DriverInsurance.txt"
bookingfile = "Booking.txt"
claiminsurancefile = "ClaimInsurance.txt"

doMenu(carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile)