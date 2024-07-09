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
    print("      Welcome to AEA Cars!!\n")
    while choice != 0:
        print("          Main Menu              ")
        print("---------------------------------")
        print("|  0 - Exit                     |")
        print("|  1 - Create Car Insurance     |")
        print("|  2 - Create Driver Insurance  |")
        print("|  3 - Claim Insurance          |")
        print("|  4 - Print Receipt            |")
        print("---------------------------------")
        choice = keyboardInput(int, "Enter your choice: ", "Invalid choice")
        print("")
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
#     try:
#         lines =None
#         with open(carfile, "rt") as filehandler:
#             # read all lines 
#             lines = filehandler.readlines()
#         for index, line in enumerate(lines):
#             car_plate_no, make, model, year, insurance_company, policy_number, vin, coverage_type, premium_amount, status, expiry_date, claim_amount = line.strip().split("|")# strip method remove the last \n (new line) & remove spaces
#             if (index == 0):
#                 print(f"{"No.":<4}{car_plate_no:<12}{make:<12}{model:<9}{year:<5}{insurance_company:<19}\
# {policy_number:<14}{vin:<20}{coverage_type:<15}{premium_amount:<16}{status:<10}\
# {expiry_date:<13}{claim_amount:<10}")
#                 print("=" * 165)
#             else:
#                 print(f"{index:<4}{car_plate_no:<12}{make:<12}{model:<10}{year:<5}{insurance_company:<19}\
# {policy_number:<14}{vin:<20}{coverage_type:<15}{premium_amount:<16}{status:<10}\
# {expiry_date:<13}{claim_amount:<10}")

#             #     print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}")
#     except Exception as e: 
#         print("Something went wrong when we print the products:", e)
    pass
def createDriverInsurance(driverfile, driverinsurancefile):
#     try:
#         lines =None
#         with open(driverfile, "rt") as filehandler:
#             # read all lines 
#             lines = filehandler.readlines()
#         for index, line in enumerate(lines):
#             driver_id, driver_name, driver_age, driver_gender, license, insurance_company, policy_number,\
#             coverage_type, premium_amount, status, expiry_date, claim_amount = line.strip().split("|")# strip method remove the last \n (new line) & remove spaces
#             if (index == 0):
#                 print(f"{"No.":<4}{driver_id:<6}{driver_name:<16}{driver_age:<5}{driver_gender:<8}{license:<18}{insurance_company:<19}\
# {policy_number:<14}{coverage_type:<15}{premium_amount:<16}{status:<10}\
# {expiry_date:<13}{claim_amount:<10}")
#                 print("=" * 159)
#             else:
#                 print(f"{index:<4}{driver_id:<6}{driver_name:<16}{driver_age:<5}{driver_gender:<8}{license:<18}{insurance_company:<19}\
# {policy_number:<14}{coverage_type:<15}{premium_amount:<16}{status:<10}\
# {expiry_date:<13}{claim_amount:<10}")
#     except Exception as e: 
#         print("Something went wrong when we print the products:", e)
    pass

def chooseBokingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile):
    verify = True
    while verify:
        with open(bookingfile, "rt") as file:
            display = file.read()
            print("\nBooking Detail:")
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
            while index == 0:
                print("Invalid!!")
                index = keyboardInput(int,"Plesase insert line number again: ", "Number must be integer and not zero")
                
            print("\nPlese check the detail carefully...")
            BookingID, CustomerID, CarPlate, DriverID, DriverName, BookingDate = data[index]
            print(f"\nBooking ID: {BookingID}\nCustomer ID: {CustomerID}\nPlate No: {CarPlate}\nDriver ID: {DriverID}\nName: {DriverName}\nBooking Date: {BookingDate}")
            confirm = keyboardInput(str, "\nDetails is true?  (y/n): ", "Please insert y or n")
            if confirm == "y":
                print("\nDetail Claim Amont:")
                carClaim = findCarInsurance(carinsurancefile, CarPlate)
                driverClaim = findDriverInsurance(driverinsurancefile, DriverID)
                totalClaim = carClaim + driverClaim
                print(f"Total Claim: {totalClaim}\n")
            
                totalClaimInsurance(claiminsurancefile,BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim)
                verify = False
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
            total = file.write(f"\n{BookingDate} | {CarPlate} | {carClaim} | {DriverID} | {driverClaim} | {totalClaim}")
            #print(total)

    except Exception as e:
        print("Something went wrong when we write to the file", e)

def printResit (claimInsurancefile):
    lines = None
    #claimInsurancefile = "ClaimInsurance.txt"
    try:
        with open(claimInsurancefile, 'rt') as filehandler:
            lines = filehandler.readlines()
        
        print("\nInvoice Summary:\n")
        for index,line in enumerate(lines):
            parts = line.strip().split("|")
            if len(parts) == 6:
                BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim = parts
                if(index == 0):
                    print(f"{"No:":5}{BookingDate:15}{CarPlate:>10}{carClaim:>25}{DriverID:>12}{driverClaim:>25}{totalClaim:>20}")
                    print("=" * 113)
                else:
                    CarPlate = CarPlate.strip()
                    print(f"{index:<5}{BookingDate:15}{CarPlate:>10}{carClaim:>25}{DriverID:>12}{driverClaim:>25}{totalClaim:>20}")
            else:
                print(f"Skipping line {index+1} due to incorrect format: {line.strip()}")
        print(" " * 85, "Total", "RMXXXXXX")
        print("")
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