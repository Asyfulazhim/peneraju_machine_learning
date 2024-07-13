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
            datas.append(line.strip().split("|"))
        

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
            line = "|".join(map(str, product)) + "\n"
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
            datacars.append(line.strip().split("|"))

        datacarinsurances = []
        for line in lineinsurance:
            datacarinsurances.append(line.strip().split("|"))


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
            line = "|".join(map(str, product)) + "\n"
            newlines.append(line)
        newlines[-1] = newlines[-1].strip()
        with open(carfile, "wt") as filehandler:
            filehandler.writelines(newlines)



    except Exception as e:
        print("Something went wrong when we edit the product:", e)



file1 = "Car.txt"
file2 = "CarInsurance.txt"
printCar(file1, file2)
