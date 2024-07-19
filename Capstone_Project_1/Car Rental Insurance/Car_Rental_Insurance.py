# Group Members:
# 1) Asyful Azhim
# 2) Nur Adnin
# 3) Eva Nazira

import time
from datetime import datetime

class InsuranceManager:
    def __init__(self, car_file, driver_file, car_insurance_file, driver_insurance_file, booking_file, claim_insurance_file):
        self.car_file = car_file
        self.driver_file = driver_file
        self.car_insurance_file = car_insurance_file
        self.driver_insurance_file = driver_insurance_file
        self.booking_file = booking_file
        self.claim_insurance_file = claim_insurance_file

    def keyboardInput(self, datatype, caption, errorMessage,defaultValue = None):
        value = None
        isInvalid = True
        while (isInvalid):
            try:
                if defaultValue == None:
                    value = datatype(input(caption))
                else:
                    value = input(caption)
                    if value.strip()=="":
                        value = defaultValue
                    else:
                        value = datatype(value)
            except:
                print(errorMessage)
            else:
                isInvalid = False   
        return value

    def doMenu(self, carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile):
        choice = -1
        
        while choice != 0:
            print("\n"," "*49,"Welcome to AEA Cars!!"," "*49,"\n")
            print("*"*120)
            print(" "*55,"\033[1mMain Menu\033[0m"," "*55)
            print("-"*120)
            print(" "*41,"|  \033[31m0 - Exit\033[0m                         |")
            print(" "*41,"|  \033[96m1 - Create Car Insurance\033[0m         |")
            print(" "*41,"|  \033[96m2 - Create Driver Insurance\033[0m      |")
            print(" "*41,"|  \033[96m3 - Claim Insurance\033[0m              |")
            print(" "*41,"|  \033[96m4 - Print Receipt\033[0m                |")
            print(" "*41,"|  \033[96m5 - Department Report\033[0m            |")
            print("-"*120)
            choice = self.keyboardInput(int, "Enter your choice: ", "Invalid choice")
            print("")
            if choice==0:
                print("Thank You!!")
            elif choice == 1:
                self.printCar(carfile, carinsurancefile)
            elif choice == 2:
                self.printDriver(driverfile, driverinsurancefile)
            elif choice == 3:
                self.chooseBokingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile)            
            elif choice == 4:
                self.printResit(claiminsurancefile)
            elif choice == 5:
                self.reportCompany(carinsurancefile, driverinsurancefile, claiminsurancefile)
            
    def printCar(self, carfile, carInsurancefile):
        try:
            print("-"*120)
            print(" "*53,"\033[1mCAR INSURANCE\033[0m\n"," "*53)
            lines =None
            with open(carfile, "rt") as filehandler:
                lines = filehandler.readlines()

            for index, line in enumerate(lines):
                
                carPlate, make, model, year, vin, mileage, expiry_date, status = line.strip().split(" | ")# strip method remove the last \n (new line) & remove spaces
                if (index == 0):
                    print(f"{"No.":>4}{carPlate:>12}{make:>12}{model:>9}{year:>5}{vin:>19}\
    {mileage:>8}{vin:>18}{expiry_date:>23}{status:>9}")
                    print("=" * 120)
                else:
                    print(f"{index:>4}{carPlate:>12}{make:>12}{model:>9}{year:>5}{vin:>19}\
    {mileage:>8}{vin:>20}{expiry_date:>19}{status:>11}")


            datas = []
            for line in lines:
                # print(line)
                datas.append(line.strip().split(" | "))

            
            index = self.keyboardInput(int, "Enter a number:", "Number must be in integer")
            while index==0:
                print("Invalid!")
                index = self.keyboardInput(int, "Enter a number:", "Number must be in integer")

            else:
                carPlate, make, model, year, vin, mileage, expiry_date, status = datas[index]

                print(f"\n{"Car plate number":23}:{carPlate}\n{"Make":23}:{make}\n{"Model":23}:{model}\n{"Year":23}:{year}\n{"VIN":23}:{vin}\
        \n{"Mileage":23}:{mileage}\n{"Insurance expiry date":23}:{expiry_date}\n{"Status":23}:{status}")
                if status.strip() == "Active":
                    print("\nThe insurance still active")
                    print("\nBack to main menu......")
                    time.sleep(2)
                else:
                    print("\nThe insurance has expired")
                    confirm = self.keyboardInput(str, "\nDo you want to renew this car insurance (y/n) ?", "Confirm must be in String")
                    while confirm != 'y' and confirm != 'n':
                        print("Invalid Character!\n")
                        confirm = self.keyboardInput(str, "Enter you choice again (y/n) ?", "Confirm must be in String")

                    if confirm == "y":
                        self.findCarInsurance(carInsurancefile, carPlate, carfile)

                    elif confirm == "n":
                        print("\nBack to main menu......")
                        time.sleep(2)

                    else:
                        print("\nInvalid!")

        except Exception as e: 
            print("Something went wrong when we print the products:", e)

    def findCarInsurance(self, carinsurancefile, carplate, carfile):
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
                    newcompany = self.keyboardInput(str, f"Company[{insurance_company}]: ", "Company must be in string ", insurance_company)
                    newpolicynumber = self.keyboardInput(str, f"Policy number[{policy_number}]: ", "Policy number must be in string", policy_number)
                    newcoverage_type = self.keyboardInput(str, f"Coverage Type[{coverage_type}]: ", "Coverage type must be in string" , coverage_type)
                    newpremiumAmount = self.keyboardInput(str, f"Premium amount[{premium_amount}]: ", "Premium amount must be in integer", premium_amount)
                    newstatus = self.keyboardInput(str, f"Status[{status}]: ", "Status must be in string", status)
                    newexpirydate = self.keyboardInput(str, f"Expiry date[{expiry_date}]: ", "Expiry date must be in string", expiry_date)
                    newclaimAmount = self.keyboardInput(int, f"Claim amount[{claim_amount}]: ", "Claim amount must be in integer", claim_amount)
                    datas[i] = [carPlate, make, model, year, newcompany, newpolicynumber, vin, newcoverage_type, newpremiumAmount, newstatus, newexpirydate, newclaimAmount]
                    break

            newlines = []
            for product in datas:
                line = " | ".join(map(str, product)) + "\n"
                newlines.append(line)
            newlines[-1] = newlines[-1].strip()
            with open(carinsurancefile, "wt") as filehandler:
                filehandler.writelines(newlines)

            self.updateCarfile(carfile, carinsurancefile, carplate)
            
            
        except Exception as e:
            print("Something went wrong when we edit the product:", e)

    def updateCarfile(self, carfile, carinsurancefile, carplate):
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

            time.sleep(2)
            print()
            print("\nUpdating the system.....")
            time.sleep(2)

            print("\nThe car insurance successfully renewed.")
            time.sleep(2)
            print()
            print("\nBack to main menu.....")
            time.sleep(2)

        except Exception as e:
            print("Something went wrong when we edit the product:", e)

    def printDriver(self, driverfile, driverInsurancefile):
        try:
            print("-"*120)
            print(" "*52,"\033[1mDRIVER INSURANCE\033[0m\n"," "*52)
            lines =None
            with open(driverfile, "rt") as filehandler:
                lines = filehandler.readlines()
            for index, line in enumerate(lines):

                driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus = line.strip().split(" | ")# strip method remove the last \n (new line) & remove spaces
                if (index == 0):
                    print(f"{"No.":<8}{driverId:<12}{drivername:<19}{driverAge:<8}{gender:<12}{license:<22}\
    {driverExpiredate:<19}{driverstatus:<14}")
                    print("=" * 120)
                else:
                    print(f"{index:<8}{driverId:<12}{drivername:<19}{driverAge:<8}{gender:<12}{license:<22}\
    {driverExpiredate:<19}{driverstatus:<14}")


            datas = []
            for line in lines:
                # print(line)
                datas.append(line.strip().split(" | "))
            
            index = self.keyboardInput(int, "Enter a number: ", "Number must be in integer")
            while index==0:
                print("Invalid!")
                index  =self.keyboardInput(int, "Enter a number:", "Number must be in integer")
            driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus = datas[index]

            print(f"\n{"Driver ID":23}:{driverId}\n{"Name":23}:{drivername}\n{"Age":23}:{driverAge}\n{"Gender":23}:{gender}\n{"License number":23}:{license}\n{"Insurance expired date":23}:{driverExpiredate}\
    \n{"Insurance status":23}:{driverstatus}")
            
            if driverstatus.strip() == "Active":
                print("\nThe insurance still active")
                print("\nBack to main menu......")
                time.sleep(2)
            else:
                print("\nThe insurance has expired")
                confirm = self.keyboardInput(str, "\nDo you want to renew this driver insurance (y/n) ?", "Confirm must be in String")
                while confirm != 'y' and confirm != 'n':
                        print("Invalid Character!\n")
                        confirm = self.keyboardInput(str, "Enter you choice again (y/n) ?", "Confirm must be in String")

                if confirm == "y":
                    self.findDriverInsurance(driverInsurancefile, driverId, driverfile)
                elif confirm == "n":
                        print("\nBack to main menu......")
                        time.sleep(2)

        except Exception as e: 
            print("Something went wrong when we print the products:", e)


    def findDriverInsurance(self, driverInsurancefile, driverId, driverfile):
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
                    newcompany = self.keyboardInput(str, f"Company[{DriverCompanyInsurance}]: ", "Company must be in string ", DriverCompanyInsurance)
                    newpolicynumber = self.keyboardInput(str, f"Policy number[{DriverPolicy}]: ", "Policy number must be in string", DriverPolicy)
                    newcoverage_type = self.keyboardInput(str, f"Coverage Type[{DriverCoverage}]: ", "Coverage type must be in string" , DriverCoverage)
                    newpremiumAmount = self.keyboardInput(str, f"Premium amount[{DriverPremium}]: ", "Premium amount must be in integer", DriverPremium)
                    newstatus = self.keyboardInput(str, f"Status[{DriverStatus}]: ", "Status must be in string", DriverStatus)
                    newexpirydate = self.keyboardInput(str, f"Expiry date[{DriverExpiryDate}]: ", "Expiry date must be in string", DriverExpiryDate)
                    newclaimAmount = self.keyboardInput(int, f"Claim amount[{driverClaim}]: ", "Claim amount must be in integer", driverClaim)
                    datas[i] = [driverID, DriverName, DriverAge, DriverContact, DriverLicense, newcompany, newpolicynumber, newcoverage_type, newpremiumAmount, newstatus, newexpirydate, newclaimAmount]
                    break
                    
            newlines = []
            for product in datas:
                line = " | ".join(map(str, product)) + "\n"
                newlines.append(line)
            newlines[-1] = newlines[-1].strip()
            with open(driverInsurancefile, "wt") as filehandler:
                filehandler.writelines(newlines)

            self.updateDriverfile(driverfile, driverInsurancefile, driverID)
            
            
        except Exception as e:
            print("Something went wrong when we edit the product:", e)

    def updateDriverfile(self, driverfile, driverInsurancefile, driverID):
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

            
            time.sleep(2)
            print()
            print("\nUpdating the system.....")
            time.sleep(2)

            print("\nThe driver insurance successfully renewed.")
            time.sleep(2)
            print()
            print("\nBack to main menu.....")
            time.sleep(2)
            

        except Exception as e:
            print("Something went wrong when we edit the product:", e)


    def chooseBokingLine(self, bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile):
        verify = True
        while verify:

            print(" "*52,"\033[1mCLAIM INSURANCE\033[0m"," "*52)
            print("\nBooking Detail:\n")
            self.readbookingfile(bookingfile)

            try:
                lines = None
                with open(bookingfile, "rt") as file:
                    lines = file.readlines()
                    #print(lines)
                data = []
                for line in lines:
                    data.append(line.strip().split("|"))
                #print(data)

                index = self.keyboardInput(int,"Plesase insert line number: ", "Number must be integer")
                while index==0:
                    print("Invalid!")
                    index = self.keyboardInput(int,"Plesase insert line number: ", "Number must be in integer")
                print("\nPlese check the detail carefully...")
                BookingID, CustomerID, CarPlate, DriverID, DriverName, BookingDate = data[index]
                print(f"\n{"Booking ID":15}: {BookingID}\n{"Customer ID":15}:{CustomerID}\n{"Plate No":15}:{CarPlate}\n{"Driver ID":15}:{DriverID}\n{"Name":15}:{DriverName}\n{"Booking Date":15}:{BookingDate}")
                confirm = self.keyboardInput(str, "\nDetails is true?  (y/n): ", "Please insert y or n")
                while confirm != "y" and confirm != "n":
                    print("Invalid Character!")
                    confirm = self.keyboardInput(str, "\nEnter confirmation again (y/n): ", "Please insert y or n")

                if confirm == "y":
                    print("\nDetail Claim Amont:")
                    carClaim = self.claimfindCarInsurance(carinsurancefile, CarPlate)
                    driverClaim = self.claimfindDriverInsurance(driverinsurancefile, DriverID)
                    totalClaim = carClaim + driverClaim
                    print(f"Total Claim: {totalClaim}\n")
                    self.totalClaimInsurance(claiminsurancefile,BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim)
                    print("Updating to the system.....")
                    time.sleep(2)
                    print("\nClaim Insurance successfully added.")
                    verify = False

            except Exception as e:
                print("Error edit product:", e)

    def readbookingfile(self, bookingfile):
        with open (bookingfile, "r") as file:
            booking = file.readlines()
        
        for index, line in enumerate(booking):
            bookingID, custID, carPlate, driverID, driverName, bookingDate = line.strip().split(" | ")
            if (index == 0):
                print(f"{"No.":<10}{bookingID:<18}{custID:<19}{carPlate:<21}{driverID:<18}{driverName:<22}{bookingDate:<21}")
                print("=" * 120)
            else:
                print(f"{index:<10}{bookingID:<18}{custID:<19}{carPlate:<21}{driverID:<18}{driverName:<22}{bookingDate:<21}")
        print("-" * 120)
        print()

    def claimfindCarInsurance (self, carinsurancefile,CarPlate):
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

    def claimfindDriverInsurance (self, driverinsurancefile, DriverID):
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

    def totalClaimInsurance (self, claimInsurancefile,BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim):
        #claimInsurancefile = "ClaimInsurance.txt"
        try:
            with open(claimInsurancefile, "at") as file:
                total = file.write(f"\n{BookingDate} | {CarPlate} | {carClaim} | {DriverID} | {driverClaim} | {totalClaim}")
                #print(total)

        except Exception as e:
            print("Something went wrong when we write to the file", e)

    def printResit (self, claimInsurancefile):
        lines = None
        print("*"*120)
        net_claimed = 0.0
        #claimInsurancefile = "ClaimInsurance.txt"
        try:
            with open(carinsurancefile,"rt") as file:
                line = file.readlines()
                print(f"\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                print("-"*120)
                print(" "*47,"\033[1mSUMMARY INSURANCE CLAIMED\033[0m"," "*47)
                print("\n"," "*45,"AEA CAR RENTAL SERVICE SDN BHD"," "*45)
                print(" "*42,"123,AEA STREET, EFG CITY,45689 HIJL"," "*42)
                print(" "*52,"(123)- 4567 890"," "*52)
                print(" "*51,"\033[94minfo@AEARENTAL.com\033[0m"," "*51)
                print("-"*120)

            with open(claimInsurancefile, 'rt') as filehandler:
                
                lines = filehandler.readlines()
            
            print("\nInvoices Summary:\n")
            for index,line in enumerate(lines):
                parts = line.strip().split("|")
                if len(parts) == 6:
                    BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim = parts
                    if(index == 0):
                        print(f"{"No:":5}{BookingDate:>11}{CarPlate:>15}{carClaim:>25}{DriverID:>12}{driverClaim:>25}{totalClaim:>2}")
                        print("=" * 116)
                    else:
                        CarPlate = CarPlate.strip()
                        print(f"{index:<5}{BookingDate:15}{CarPlate:>10}{carClaim:>25}{DriverID:>14}{driverClaim:>23}{totalClaim:>22}")
                        #print("-"*116)
            
            for line in lines[1:]:
                line = line.strip().split("|")
                net_claimed += float(line[5].strip())
            print(" "*77,f"Net total claimed:     \033[92mRM {net_claimed:,.2f}\033[0m")
            print("-"*120)
            print("Thank you for your bussiness!")
            print("-"*120)
            print("Signature:\n\n\n")
            print("_"*30)
            print("Name:")
            print("Date:")

            
            time.sleep(2)
            print()
            print("\nBack to main menu.....")
            time.sleep(2)
            
        except Exception as e:
            print("Something went wrong when we read from the file", e)
    #______________________________________________________________________________#
    def reportCompany (self, carinsurancefile, driverinsurancefile, claiminsurancefile):
        print('-'*45, "\033[1mREPORT ON INSURANCE DEPARTMENT\033[0m",'-'*45)
        print()
        try:
            year = self.keyboardInput(int,"Report Year: ","Please input Year in YYYY format")
            while len(str(year)) != 4 :
                print("Invalid!")
                year = self.keyboardInput(int,"Report Year: ","Please input Year in YYYY format")
            #to get the report on the month that user want
            targetDate = datetime(year,1,1)
            totalCarsWithInsurance = 0
            totalActiveCars = 0
            totalInactiveCar = 0
            totalDriverWithInsurance = 0
            totalActiveDriver = 0
            totalInactiveDriver = 0
            totalRenewInsuranceCar = 0
            totalClaims = 0
            while year ==2024:
                with open(carinsurancefile,'rt') as file:
                    next(file)
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
                        else:
                            print (f"The report for Year {year} is not available.")
                            break
                
                with open(driverinsurancefile,'rt') as file:
                    next(file)
                    for line in file:
                        data = line.strip().split("|")
                        if len(data)<12:
                            continue

                        expiry_date_str = data[-2].strip()
                        status = data[-3].strip()
                        try:
                            expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d')

                        except:
                            print(f"Invalide date format encountered:{expiry_date_str}. Skip line")
                            continue
                        if expiry_date.year<=year or expiry_date.year>=year:
                            totalDriverWithInsurance += 1
                            if status == 'Active':
                                totalActiveDriver += 1
                            elif status == 'Inactive':
                                totalInactiveDriver += 1
                        else:
                            print(f"The report for year {year} is not available.")
                            break
                totalRenewInsuranceCar = totalInactiveCar + totalInactiveDriver
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


                # Display in table
                totalCarsWithInsurance = str(totalCarsWithInsurance)
                totalActiveCars = str(totalActiveCars)
                totalInactiveCar = str(totalInactiveCar)
                totalDriverWithInsurance = str(totalDriverWithInsurance)
                totalActiveDriver = str(totalActiveDriver)
                totalInactiveDriver = str(totalInactiveDriver)
                totalClaims = str(totalClaims)

                print("="*120)
                print(f"|{'Cars'.center(36)}|{'Driver'.center(36)}|{'Claim Made'.center(44)}|")
                print("-"*75)
                print(f"|{'Active'.center(17)}|{'Expired'.center(18)}|{'Active'.center(18)}|{'Expired'.center(17)}|{'|':>45}")
                print("="*120)
                print(f"|{totalActiveCars.center(17)}|{totalInactiveCar.center(17)} |{totalActiveDriver.center(17)} |{totalInactiveDriver.center(17)}|{totalClaims.center(44)}|")
                print("-"*75)
                print(f"|{totalCarsWithInsurance.center(36)}|{totalDriverWithInsurance.center(36)}|{"|":>45}")
                print("-"*120)
                
                # Adding some details
                print("\nDetails:")
                print(f"1. Cars: The report shows the status of cars in the insurance system.")
                print(f"2. There are {totalActiveCars} active car insurance policies and {totalInactiveCar} expired car insurance policies.")
                print(f"3. Driver: The report also details the driver insurance policies.")
                print(f"4. There are {totalActiveDriver} active driver insurance policies and {totalInactiveDriver} expired driver insurance policies.")
                print(f"5. Claim Made: In the current year, a total of {totalClaims} claims have been made under the insurance policies.")

                # Additional summary
                # print(f"\nSummary:")
                # print(f"The insurance department has been actively managing the policies with a total of {totalCarsWithInsurance} car insurance policies and {totalDriverWithInsurance} driver")
                # print(f"insurance policies and {totalDriverWithInsurance} driver insurance policies.")
                # print(f"Efforts to ensure timely renewals and addressing the claims promptly are reflected in the above statistics.")

                print(f"""
Summary:
The insurance department has been actively managing the policies with a total of {totalCarsWithInsurance} car insurance policies 
and {totalDriverWithInsurance} driver insurance policies. Efforts to ensure timely renewals and addressing the claims promptly 
are reflected in the above statistics.
        """)

                time.sleep(2)
                print()
                print("\nBack to main menu.....")
                time.sleep(2)
                break
            else:
                print("\033[91mNo record!\033[0m")

        except FileNotFoundError:
            print("Error: One or more insurance file not found")

        except Exception as e:
            print(f"An error occured: {e}")

        except FileNotFoundError:
            print("Error: One or more insurance file not found")

        except Exception as e:
            print(f"An error occured: {e}")


carfile = "Car.txt"
driverfile = "Driver.txt"
carinsurancefile = "CarInsurance.txt"
driverinsurancefile = "DriverInsurance.txt"
bookingfile = "Booking.txt"
claiminsurancefile = "ClaimInsurance.txt"

admin = InsuranceManager(carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile)
admin.doMenu(carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile)