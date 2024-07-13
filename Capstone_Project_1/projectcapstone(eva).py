import time
from datetime import datetime
#--------------------------------------------------------------------------------------------------------#
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
#--------------------------------------------------------------------------------------------------------#

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
            createCarInsurance(carfile, carinsurancefile)
        elif choice == 2:
            createDriverInsurance(driverfile, driverinsurancefile)
        elif choice == 3:
            chooseBookingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile)            
        elif choice == 4:
            printResit(claiminsurancefile,carinsurancefile,driverinsurancefile)
        elif choice == 5:
            reportCarInsurance(carinsurancefile, driverinsurancefile, claiminsurancefile)
#--------------------------------------------------------------------------------------------------------#

def readbookingfile(bookingfile):
    with open (bookingfile, "r") as file:
        booking = file.read()
        print (booking)
#--------------------------------------------------------------------------------------------------------#

def createCarInsurance(carfile, carinsurancefile):
    try:
        lines =None
        with open(carfile, "rt") as filehandler:
            # read all lines 
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            car_plate_no, make, model, year, insurance_company, policy_number, vin, coverage_type, premium_amount, status, expiry_date, claim_amount = line.strip().split("|")# strip method remove the last \n (new line) & remove spaces
            if (index == 0):
                print(f"{"No.":<4}{car_plate_no:<12}{make:<12}{model:<9}{year:<5}{insurance_company:<19}\
{policy_number:<14}{vin:<20}{coverage_type:<15}{premium_amount:<16}{status:<10}\
{expiry_date:<13}{claim_amount:<10}")
                print("=" * 165)
            else:
                print(f"{index:<4}{car_plate_no:<12}{make:<12}{model:<10}{year:<5}{insurance_company:<19}\
{policy_number:<14}{vin:<20}{coverage_type:<15}{premium_amount:<16}{status:<10}\
{expiry_date:<13}{claim_amount:<10}")

            #     print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e: 
        print("Something went wrong when we print the products:", e)

#--------------------------------------------------------------------------------------------------------#

def createDriverInsurance(driverfile, driverinsurancefile):
    try:
        lines =None
        with open(driverfile, "rt") as filehandler:
            # read all lines 
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            driver_id, driver_name, driver_age, driver_gender, license, insurance_company, policy_number,\
            coverage_type, premium_amount, status, expiry_date, claim_amount = line.strip().split("|")# strip method remove the last \n (new line) & remove spaces
            if (index == 0):
                print(f"{"No.":<4}{driver_id:<6}{driver_name:<16}{driver_age:<5}{driver_gender:<8}{license:<18}{insurance_company:<19}\
{policy_number:<14}{coverage_type:<15}{premium_amount:<16}{status:<10}\
{expiry_date:<13}{claim_amount:<10}")
                print("=" * 159)
            else:
                print(f"{index:<4}{driver_id:<6}{driver_name:<16}{driver_age:<5}{driver_gender:<8}{license:<18}{insurance_company:<19}\
{policy_number:<14}{coverage_type:<15}{premium_amount:<16}{status:<10}\
{expiry_date:<13}{claim_amount:<10}")
    except Exception as e: 
        print("Something went wrong when we print the products:", e)



# tukar def chooseBookingLine
# user input suppose to be booking ID, 
# then system will show if the booking ID is existed in list or not


# def chooseBokingLine(bookingfile,carinsurancefile,driverinsurancefile, claiminsurancefile):
#     verify = True
#     while verify:
#         with open(bookingfile, "rt") as file:
#             display = file.read()
#             print("\nBooking Detail:")
#             print(display)
#         try:
#             lines = None
#             with open(bookingfile, "rt") as file:
#                 lines = file.readlines()
#                 #print(lines)
#             data = []
#             for line in lines:
#                 data.append(line.strip().split("|"))
#             #print(data)

#             index = keyboardInput(int,"Plesase insert line number: ", "Number must be integer")
#             print("\nPlese check the detail carefully...")
#             BookingID, CustomerID, CarPlate, DriverID, DriverName, BookingDate = data[index]
#             print(f"\nBooking ID: {BookingID}\nCustomer ID: {CustomerID}\nPlate No: {CarPlate}\nDriver ID: {DriverID}\nName: {DriverName}\nBooking Date: {BookingDate}")
#             confirm = keyboardInput(str, "\nDetails is true?  (y/n): ", "Please insert y or n")
#             if confirm == "y":
#                 print("\nDetail Claim Amont:")
#                 carClaim = findCarInsurance(carinsurancefile, CarPlate)
#                 driverClaim = findDriverInsurance(driverinsurancefile, DriverID)
#                 totalClaim = carClaim + driverClaim
#                 print(f"Total Claim: {totalClaim}\n")
            
#                 totalClaimInsurance(claiminsurancefile,BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim)
#                 verify = False
#             #BookingID | CustomerID | CarPlate | DriverID | DriverName | BookingDate

#         except Exception as e:
#             print("Error edit product:", e)
#--------------------------------------------------------------------------------------------------------#

def chooseBookingLine(bookingfile,carinsurancefile,driverinsurancefile,claiminsurancefile):
    verify = True
    while verify:
        try:
            bookingInput = keyboardInput(str,"Enter your Booking ID: ","Your Booking ID is not in system")
            bookingID = bookingInput.strip().upper()
        
            with open(bookingfile,"rt") as file:
                lines = file.readlines()

            found = False
            for line in lines:
                bookingDetails = line.strip().split("|")
                if bookingDetails[0].strip() == bookingID.strip():
                    found = True
                    BookingID, CustomerID, CarPlate, DriverId, DriverName, BookingDate = bookingDetails
                    print(f"\nBooking ID:{BookingID}\nCustomer ID:{CustomerID}\nPlate no:{CarPlate}\nDriver ID:{DriverId}\nDriver Name:{DriverName}\nBooking Date:{BookingDate}")
                    confirm = input("\nDetails of booking correct (y/n) ?").strip().lower()
                    if confirm == 'y':
                        print("\nDetails of amount that can be claimed: ")
                        carClaim = findCarInsurance(carinsurancefile,CarPlate)
                        driverClaim = findDriverInsurance(driverinsurancefile, DriverId)
                        totalclaim = carClaim + driverClaim
                        print(f"\nTotal that can be claimed: {totalclaim}\n")

                        totalClaimInsurance(claiminsurancefile,BookingDate,CarPlate, carClaim,DriverId,driverClaim,totalclaim)
                        verify = False
                    break
            if not found:
                print(f"Bookinng ID {bookingID} not found")

        except Exception as e:
            print("Something went wrong when you keyin the Booking ID", e)
            

#--------------------------------------------------------------------------------------------------------#

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
#--------------------------------------------------------------------------------------------------------#

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
#--------------------------------------------------------------------------------------------------------#

def totalClaimInsurance (claimInsurancefile,BookingDate, CarPlate, carClaim, DriverID, driverClaim, totalClaim):
    #claimInsurancefile = "ClaimInsurance.txt"
    try:
        with open(claimInsurancefile, "at") as file:
            total = file.write(f"\n{BookingDate} | {CarPlate} | {carClaim} | {DriverID} | {driverClaim} | {totalClaim}")
            #print(total)

    except Exception as e:
        print("Something went wrong when we write to the file", e)
#--------------------------------------------------------------------------------------------------------#

def printResit (claimInsurancefile,carinsurancefile,driverinsurancefile):
    #claimInsurancefile = "ClaimInsurance.txt"
    lines = None
    print("MONTHLY INSURANCE CLAIM INVOICE")
    print("="*80)
    print(f"\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print("-"*80)
    total_claimed= 0.0
    #==============================================================================#
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
            next(filehandler)
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
            for line in lines:
    
                    line = line.strip().split("|")
                    total_claimed += float(line[5].strip()) 
            print(f"Net Total claimed: {total_claimed:>40}")

            #     else:
            #         print(f"Skipping line {index+1} due to incorrect format: {line.strip()}")
            # print(" " * 85, "Total", "RM")
            time.sleep(5)
    except Exception as e:
        print("Something went wrong when we read from the file", e)

#--------------------------------------------------------------------------------------------#

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
#-------------------------------------------------------------------------------------------#
# def monthlyReport(carinsurancefile,driverinsurancefile,claiminsurancefile,year,month):
#     print('-'*20, "MONTHLY REPORT ON INSURANCE DEPARTMENT",'-'*20)  
    
#     try:

#         #to get the report on the month that user want
#         targetDate = datetime(year,month,1)
#         totalCarsWithInsurance = 0
#         totalActiveCars = 0
#         totalInactiveCar = 0
#         totalRenewInsuranceCar = 0
#         totalDriverWithInsurance = 0
#         totalClaims = 0

#         with open(carinsurancefile,'rt') as file:
#             next(file)#skip header line
#             for line in file:
#                 data = line.strip().split("|")
#                 if len(data)<12:
#                     continue

#                 expiry_date_str = data[-2].strip()
#                 status = data[-3].strip()

#                 try: 
#                     expiry_date= datetime.strptime(expiry_date_str, '%Y-%m-%d')

#                 except:
#                     print(f"Invalid date format encountered:{expiry_date_str}. Skip line")
#                     continue
#                 if expiry_date.year>=year and expiry_date.month>=month:
#                     totalCarsWithInsurance += 1
#                     if status == 'Active':
#                         totalActiveCars += 1
#                         # if expiry_date.year==year and expiry_date.month==month:
                            
#                         #     totalRenewInsuranceCar += 1
#                         #     print("cars",data[0])
#                     elif status == 'Inactive':
#                         totalInactiveCar += 1
#                         if expiry_date.year<=year and expiry_date.month<=month:
#                             totalRenewInsuranceCar += 1
        
#         # with open(driverinsurancefile,'rt') as file:
#         #     for line in file:
#         #         data = line.strip().split("|")
#         #         expiry_date = datetime.strptime(data[-2], '%Y-%m-%d')
#         #         if expiry_date.year==year and expiry_date.month==month:
#         #             totalDriverWithInsurance += 1

#         with open(claiminsurancefile,'rt') as file:
#             next(file)
#             for line in file:
#                 data = line.strip().split("|")
#                 if len(data)<6:
#                     continue

#                 booking_date_str = data[0].strip()
#                 try:
#                     booking_date = datetime.strptime(booking_date_str, '%Y-%m-%d')

#                 except ValueError:
#                     print(f"Invalid date format encountered: {booking_date_str}. Skip line.")
#                     continue

#                 if booking_date.year==year and booking_date.month==month:
#                     totalClaims += 1

#         #display
#         print("="*72)
#         print(f"\nMonthly Report for {targetDate.strftime('%B %Y')}")

#         print(f"\nTotal cars with insurance: {totalCarsWithInsurance}")
#         print(f" - Cars with Active insurance: {totalActiveCars} cars")
#         print(f" - Cars with Inactive insurance: {totalInactiveCar} cars")
#         print(f"Total cars that will need to renew insurance this month: {totalRenewInsuranceCar} cars")
#         # print(f"Total drivers with insurance: {totalDriverWithInsurance}")
#         print(f"Total claims that has been made: {totalClaims}")

#     except FileNotFoundError:
#         print("Error: One or more insurance file not found")

#     except Exception as e:
#         print(f"An error occured: {e}")

#---------------------------------------------------------------------------------------#

carfile = "Car.txt"
driverfile = "Driver.txt"
carinsurancefile = "CarInsurance.txt"
driverinsurancefile = "DriverInsurance.txt"
bookingfile = "Booking.txt"
claiminsurancefile = "ClaimInsurance.txt"        

print("*"*72)
doMenu(carfile,driverfile,carinsurancefile,driverinsurancefile,bookingfile, claiminsurancefile)