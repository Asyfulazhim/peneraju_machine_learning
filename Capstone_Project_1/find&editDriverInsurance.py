# filename = CarInsurance.txt

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

        index = keyboardInput(int, "Enter a number: ", "Number must be in integer")
        driverId, drivername, driverAge, gender, license, driverExpiredate, driverstatus = datas[index]

        print(f"\nDriver ID: {driverId}\nName: {drivername}\nAge: {driverAge}\nGender: {gender}\niLicense number: {license}\nInsurance expired date: {driverExpiredate}\
\nInsurance status: {driverstatus}")
        
        if driverstatus.strip() == "Active":
            print("\nThe insurance has been active")
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



file1 = "Driver.txt"
file2 = "DriverInsurance.txt"
printDriver(file1, file2)
