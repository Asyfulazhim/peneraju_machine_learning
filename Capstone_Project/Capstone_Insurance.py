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
            printCar(carfile, carinsurancefile)
        elif choice == 2:
            createDriverInsurance(driverfile, driverinsurancefile)
        elif choice == 3:
            chooseBokingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile)            
        elif choice == 4:
            printResit(claiminsurancefile)
        
def printCar(carfile, carInsurancefile):
    try:
        lines =None
        with open(carfile, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            carPlate, make, model, year, vin, mileage, expiry_date, status = line.strip().split(" | ")# strip method remove the last \n (new line) & remove spaces
            if (index == 0):
                print(f"{"No.":<4}{carPlate:<12}{make:<12}{model:<9}{year:<5}{vin:<19}\
{mileage:<10}{vin:<20}{expiry_date:<25}{status:<10}")
                print("=" * 140)
            else:
                print(f"{index:<4}{carPlate:<12}{make:<12}{model:<9}{year:<5}{vin:<19}\
{mileage:<10}{vin:<20}{expiry_date:<25}{status:<10}")


        datas = []
        for line in lines:
            # print(line)
            datas.append(line.strip().split(" | "))

        index = keyboardInput(int, "Enter a number:", "Number must be in integer")
        carPlate, make, model, year, vin, mileage, expiry_date, status = datas[index]

        print(f"\nCar plate number: {carPlate}\nMake: {make}\nModel: {model}\nYear: {year}\nVIN: {vin}\
\nMileage: {mileage}\nInsurance expiry date: {expiry_date}\nStatus: {status}")
        if status.strip() == "Active":
            print("\nThe insurance has been active")
        else:
            print("\nThe insurance has been expired")
            confirm = keyboardInput(str, "\nDo you want to renew this car insurance (y/n) ?", "Confirm must be in String")
            if confirm == "y":
                findCarInsurance(carInsurancefile, carPlate, carfile)

    except Exception as e: 
        print("Something went wrong when we print the products:", e)

def findCarInsurance(carinsurancefile, carplate, carfile):
    carPlate = carplate.replace(" ","")
    try:
        with open(carinsurancefile, "rt") as file:
            lines = file.readlines()

        datas = []
        for line in lines:
            datas.append(line.strip().split(" | "))
        

        for i, data in enumerate(datas): # i for row
            if data[0].replace(" ","") == carPlate:
                
                carPlate, make, model, year, insurance_company, policy_number, vin,coverage_type, premium_amount, status, expiry_date, claim_amount = data
                newcompany = keyboardInput(str, f"Company[{insurance_company}]: ", "Company must be in string ", insurance_company)
                newpolicynumber = keyboardInput(str, f"Policy number[{policy_number}]: ", "Policy number must be in string", policy_number)
                newcoverage_type = keyboardInput(str, f"Coverage Type[{coverage_type}]: ", "Coverage type must be in string" , coverage_type)
                newpremiumAmount = keyboardInput(str, f"Premium amount[{premium_amount}]: ", "Premium amount must be in integer", premium_amount)
                newstatus = keyboardInput(str, f"Status[{status}]: ", "Status must be in string", status)
                newexpirydate = keyboardInput(str, f"Expiry date[{expiry_date}]: ", "Expiry date must be in string", expiry_date)
                newclaimAmount = keyboardInput(int, f"Claim amount[{claim_amount}]: ", "Claim amount must be in integer", claim_amount)
                datas[i] = [carPlate, make, model, year, newcompany, newpolicynumber, vin, newcoverage_type, newpremiumAmount, newstatus, newexpirydate, newclaimAmount]
                break

        newlines = []
        for product in datas:
            line = " | ".join(map(str, product)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(carinsurancefile, "wt") as filehandler:
            filehandler.writelines(newlines)

        updateCarfile(carfile, carinsurancefile, carplate)
        
        
    except Exception as e:
        print("Something went wrong when we edit the product:", e)

def updateCarfile(carfile, carinsurancefile, carplate):
    carPlate = carplate.replace(" ","")

    try:
        with open(carfile, "rt") as filecar:
            linecar = filecar.readlines()

        with open(carinsurancefile, "rt") as fileinsurance:
            lineinsurance = fileinsurance.readlines()

        datacars = []
        for line in linecar:
            datacars.append(line.strip().split(" | "))

        datacarinsurances = []
        for line in lineinsurance:
            datacarinsurances.append(line.strip().split(" | "))


        for i, datacar in enumerate(datacars): # i for row
            for j, datacarinsurance in enumerate(datacarinsurances):
                if datacar[0].replace(" ","") == carPlate and datacarinsurance[0].replace(" ","") == carPlate:
                
                    Carplate, carmake, carmodel, caryear, carvin, mileage, carexpiry_date, carstatus = datacar
                    carPlate, make, model, year, insurance_company, policy_number, vin,coverage_type, premium_amount, status, expiry_date, claim_amount = datacarinsurance
                    carexpiry_date = expiry_date
                    carstatus = status
                    datacars[i] = [Carplate, carmake, carmodel, caryear, carvin, mileage, carexpiry_date, carstatus]
        
        newlines = []
        for product in datacars:
            line = " | ".join(map(str, product)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(carfile, "wt") as filehandler:
            filehandler.writelines(newlines)



    except Exception as e:
        print("Something went wrong when we edit the product:", e)

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
        # with open(bookingfile, "rt") as file:
        #     display = file.read()
        #     print("\nBooking Detail:")
        #     print(display)
        print("\nBooking Detail:\n")
        readbookingfile(bookingfile)

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

def readbookingfile(bookingfile):
    with open (bookingfile, "r") as file:
        booking = file.readlines()
    
    for index, line in enumerate(booking):
        bookingID, custID, carPlate, driverID, driverName, bookingDate = line.strip().split(" | ")
        if (index == 0):
            print(f"{"No.":<4}{bookingID:<12}{custID:<13}{carPlate:<15}{driverID:<12}{driverName:<18}{bookingDate:<15}")
            print("=" * 85)
        else:
            print(f"{index:<4}{bookingID:<12}{custID:<13}{carPlate:<15}{driverID:<12}{driverName:<18}{bookingDate:<15}")
    print("-" * 90)
    print()

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