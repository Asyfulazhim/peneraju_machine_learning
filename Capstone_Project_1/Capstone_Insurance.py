import time
from datetime import datetime

def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if value.strip() == "":
                    value = defaultValue
                else:
                    value = datatype(value)
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
        print("|  5 - Insurance Dept. Report   |")
        print("---------------------------------")
        choice = keyboardInput(int, "Enter your choice: ", "Invalid choice")
        print("")
        if choice==0:
            print("Thank You!!")
        elif choice == 1:
            printCar(carfile, carinsurancefile)
        elif choice == 2:
            printDriver(driverfile, driverinsurancefile)
        elif choice == 3:
            chooseBokingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile)            
        elif choice == 4:
            printResit(claiminsurancefile,carinsurancefile,driverinsurancefile)
        elif choice == 5:
            reportCarInsurance(carinsurancefile, driverinsurancefile, claiminsurancefile)

#--------------------------------choice1--------------------------------------------------------------------------    
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
        while index == 0:
            print("Invalid!!")
            index = keyboardInput(int,"Please enter a number again: ", "Number must be integer and not zero")
        
        carPlate, make, model, year, vin, mileage, expiry_date, status = datas[index]

        print(f"\nCar plate number: {carPlate}\nMake: {make}\nModel: {model}\nYear: {year}\nVIN: {vin}\
\nMileage: {mileage}\nInsurance expiry date: {expiry_date}\nStatus: {status}")
        if status.strip() == "Active":
            print("\nThe insurance is still active")
            print("back to main menu.....\n")
            time.sleep(2)
            
        else:
            print("\nThe insurance has expired")
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

#--------------------------------choice2--------------------------------------------------------------------------
def printDriver(driverfile, driverInsurancefile):
    try:
        lines =None
        with open(driverfile, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):

            driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus = line.strip().split(" | ")# strip method remove the last \n (new line) & remove spaces
            if (index == 0):
                print(f"{"No.":<4}{driverId:<8}{drivername:<15}{driverAge:<4}{gender:<8}{license:<19}\
{driverExpiredate:<15}{driverstatus:<10}")
                print("=" * 100)
            else:
                print(f"{index:<4}{driverId:<8}{drivername:<15}{driverAge:<4}{gender:<8}{license:<19}\
{driverExpiredate:<15}{driverstatus:<10}")

        datas = []
        for line in lines:
            # print(line)
            datas.append(line.strip().split(" | "))

        index = keyboardInput(int, "Enter a number:", "Number must be in integer")
        while index == 0:
            print("Invalid!!")
            index = keyboardInput(int,"Please enter a number again: ", "Number must be integer and not zero")

        driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus = datas[index]

        print(f"\nDriver ID: {driverId}\nName: {drivername}\nAge: {driverAge}\nGender: {gender}\niLicense number: {license}\nInsurance expired date: {driverExpiredate}\
\nInsurance status: {driverstatus}")
        
        if driverstatus.strip() == "Active":
            print("\nThe insurance is still active")
            print("back to main menu.....\n")
            time.sleep(2)
        else:
            print("\nThe insurance has been expired")
            confirm = keyboardInput(str, "\nDo you want to renew this driver insurance (y/n) ?", "Confirm must be in String")
            if confirm == "y":
                findDriverInsurance(driverInsurancefile, driverId, driverfile)

    except Exception as e: 
        print("Something went wrong when we print the products:", e)

def findDriverInsurance(driverInsurancefile, driverId, driverfile):
    driverID = driverId.replace(" ","")
    try:
        with open(driverInsurancefile, "rt") as file:
            lines = file.readlines()

        datas = []
        for line in lines:
            datas.append(line.strip().split(" | "))

        for i, data in enumerate(datas): # i for row
            if data[0].replace(" ","") == driverID:
                
                driverID, DriverName, DriverAge, DriverContact, DriverLicense, DriverCompanyInsurance, DriverPolicy, DriverCoverage, DriverPremium, DriverStatus, DriverExpiryDate, driverClaim = data
                newcompany = keyboardInput(str, f"Company[{DriverCompanyInsurance}]: ", "Company must be in string ", DriverCompanyInsurance)
                newpolicynumber = keyboardInput(str, f"Policy number[{DriverPolicy}]: ", "Policy number must be in string", DriverPolicy)
                newcoverage_type = keyboardInput(str, f"Coverage Type[{DriverCoverage}]: ", "Coverage type must be in string" , DriverCoverage)
                newpremiumAmount = keyboardInput(str, f"Premium amount[{DriverPremium}]: ", "Premium amount must be in integer", DriverPremium)
                newstatus = keyboardInput(str, f"Status[{DriverStatus}]: ", "Status must be in string", DriverStatus)
                newexpirydate = keyboardInput(str, f"Expiry date[{DriverExpiryDate}]: ", "Expiry date must be in string", DriverExpiryDate)
                newclaimAmount = keyboardInput(int, f"Claim amount[{driverClaim}]: ", "Claim amount must be in integer", driverClaim)
                datas[i] = [driverID, DriverName, DriverAge, DriverContact, DriverLicense, newcompany, newpolicynumber, newcoverage_type, newpremiumAmount, newstatus, newexpirydate, newclaimAmount]
                break
                
        newlines = []
        for product in datas:
            line = " | ".join(map(str, product)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(driverInsurancefile, "wt") as filehandler:
            filehandler.writelines(newlines)

        updateDriverfile(driverfile, driverInsurancefile, driverID)
            
    except Exception as e:
        print("Something went wrong when we edit the product:", e)

def updateDriverfile(driverfile, driverInsurancefile, driverID):
    driverID = driverID.replace(" ","")

    try:
        with open(driverfile, "rt") as filedriver:
            linedriver = filedriver.readlines()

        with open(driverInsurancefile, "rt") as fileinsurance:
            lineinsurance = fileinsurance.readlines()

        datadrivers = []
        for line in linedriver:
            datadrivers.append(line.strip().split(" | "))

        datadriverinsurances = []
        for line in lineinsurance:
            datadriverinsurances.append(line.strip().split(" | "))


        for i, datadriver in enumerate(datadrivers): # i for row
            for j, datadriverinsurance in enumerate(datadriverinsurances):
                if datadriver[0].replace(" ","") == driverID and datadriverinsurance[0].replace(" ","") == driverID:
                
                    driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus = datadriver
                    DriverID, DriverName, DriverAge, DriverContact, DriverLicense, DriverCompanyInsurance, DriverPolicy, DriverCoverage, DriverPremium, DriverStatus, DriverExpiryDate, driverClaim = datadriverinsurance
                    driverstatus = DriverStatus
                    driverExpiredate = DriverExpiryDate
                    datadrivers[i] = [driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus]
        
        newlines = []
        for product in datadrivers:
            line = " | ".join(map(str, product)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(driverfile, "wt") as filehandler:
            filehandler.writelines(newlines)



    except Exception as e:
        print("Something went wrong when we edit the product:", e)


#--------------------------------choice3--------------------------------------------------------------------------
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
            while index == 0:
                print("Invalid!!")
                index = keyboardInput(int,"Plesase insert line number again: ", "Number must be integer and not zero")

            print("\nPlese check the detail carefully...")
            BookingID, CustomerID, CarPlate, DriverID, DriverName, BookingDate = data[index]
            print(f"\nBooking ID: {BookingID}\nCustomer ID: {CustomerID}\nPlate No: {CarPlate}\nDriver ID: {DriverID}\nName: {DriverName}\nBooking Date: {BookingDate}")
            confirm = keyboardInput(str, "\nDetails is true?  (y/n): ", "Please insert y or n")
            if confirm == "y":
                print("\nDetail Claim Amont:")
                carClaim = findCarClaimInsurance(carinsurancefile, CarPlate)
                driverClaim = findDriverClaimInsurance(driverinsurancefile, DriverID)
                totalClaim = carClaim + driverClaim
                print(f"Total Claim: {totalClaim}\n")

                print("Updating invoice.....")
                time.sleep(3)
                print("Invoice updated successfully!!\n")
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

def findCarClaimInsurance (carinsurancefile,CarPlate):
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

def findDriverClaimInsurance (driverinsurancefile, DriverID):
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

#--------------------------------choice4------------------------------------------------------------------------------------------
def printResit (claimInsurancefile,carinsurancefile,driverinsurancefile):
    lines = None
    print("MONTHLY INSURANCE CLAIM INVOICE")
    print("="*80)
    print(f"\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print("-"*80)
    total_claimed= 0.0

    try:
        with open(carinsurancefile, 'rt') as file:
            lines = file.readlines()
            print("\n\nABC CAR RENTAL SERVICE SDN BHD")
            print("123,ABD STREET, EFG CITY,45689 HIJL")
            print("(123)- 4567 890")
            print("info@ABCRENTAL.com")
            print("-"*80)

            print("Insurance Company Provider: ")
            print("-"*40)

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
        # print(" " * 85, "Total", "RMXXXXXX")
        # print(f"{"Total":>90} RM{total_claimed:>20}")
        # print("")

        for line in lines[1:]:
            line = line.strip().split("|")
            total_claimed += float(line[5].strip()) 

        print(f"{"Total":>87} (RM){total_claimed:>20}")

        print(f"Net Total claimed (RM): {total_claimed:.2f}")   
        print()
            # else:
            #     print(f"Skipping line {index+1} due to incorrect format: {line.strip()}") 
        time.sleep(2)
    except Exception as e:
        print("Something went wrong when we read from the file", e)

#-------------------------------choice5------------------------------------------------------------------------------------------
def reportCarInsurance(carinsurancefile, driverinsurancefile,claiminsurancefile):

    print('-'*20, "REPORT ON INSURANCE DEPARTMENT",'-'*20)
    try:
        year = keyboardInput(int,"Report Year: ","Please input Year in integer")
        #to get the report on the month that user want
        targetDate = datetime(year,1,1)
        totalCarsWithInsurance = 0
        totalActiveCars = 0
        totalInactiveCar = 0
        totalDriverWithInsurance = 0
        totalClaims = 0

        with open(carinsurancefile,'rt') as file:
            next(file)#skip header line
            for line in file:
                data = line.strip().split("|")
                if len(data)<12:
                    continue

                expiry_date_str = data[-2].strip()
                status = data[-3].strip()

                try: 
                    expiry_date= datetime.strptime(expiry_date_str, '%Y-%m-%d')

                except:
                    print(f"Invalid date format encountered:{expiry_date_str}. Skip line")
                    continue
                if expiry_date.year<=year or expiry_date.year>=year:
                    totalCarsWithInsurance += 1
                    if status == 'Active':
                        totalActiveCars += 1
                    elif status == 'Inactive':
                        totalInactiveCar += 1
                        # if expiry_date.year<=year or expiry_date.year>=year :
                        #     totalRenewInsuranceCar += 1
                else:
                    print (f"The report for Year {year} is not available.")
        
        # with open(driverinsurancefile,'rt') as file:
        #     for line in file:
        #         data = line.strip().split("|")
        #         expiry_date = datetime.strptime(data[-2], '%Y-%m-%d')
        #         if expiry_date.year==year and expiry_date.month==month:
        #             totalDriverWithInsurance += 1

        with open(claiminsurancefile,'rt') as file:
            next(file)
            for line in file:
                data = line.strip().split("|")
                if len(data)<6:
                    continue

                booking_date_str = data[0].strip()
                try:
                    booking_date = datetime.strptime(booking_date_str, '%Y-%m-%d')

                except ValueError:
                    print(f"Invalid date format encountered: {booking_date_str}. Skip line.")
                    continue

                if booking_date.year==year:
                    totalClaims += 1

        #display
        print("="*72)
        print(f"\nReport for {targetDate.strftime('%B %Y')}")

        print(f"\n1.\tTotal cars with insurance: {totalCarsWithInsurance}")
        print(f"\t- Cars with Active insurance: {totalActiveCars} cars")
        print(f"\t - Cars with Inactive insurance: {totalInactiveCar} cars")
        #print(f"Total cars that will need to renew insurance this month: {totalRenewInsuranceCar} cars")
        # print(f"Total drivers with insurance: {totalDriverWithInsurance}")
        print(f"2.\tTotal claims that has been made: {totalClaims}")

    except FileNotFoundError:
        print("Error: One or more insurance file not found")

    except Exception as e:
        print(f"An error occured: {e}")

    except FileNotFoundError:
        print("Error: One or more insurance file not found")

    except Exception as e:
        print(f"An error occured: {e}")

#--------------------------------Main Code---------------------------------------------------------------------------------------
carfile = "Car.txt"
driverfile = "Driver.txt"
carinsurancefile = "CarInsurance.txt"
driverinsurancefile = "DriverInsurance.txt"
bookingfile = "Booking.txt"
claiminsurancefile = "ClaimInsurance.txt"

doMenu(carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile)