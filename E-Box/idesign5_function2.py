
def daysInYear(year,leap=False):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 ==0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

year = int(input("Please enter any year: "))
daysInYear(year,leap=True)

