# Question 1

def date_decoder():
    date_str = input()
    year, month_abbr, day = date_str.split("-")
    year = int(year)
    if year <= 21:
        year += 2000
    else:
        year += 1900
    
    month_dict = {
        "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
        "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12
    }
    month = month_dict[month_abbr]
    
    return year, month, int(day)

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    year, month, day = date_decoder()
    is_leap = leap_year(year)
    
    print(f"({day:02}, {month:02}, {year}) is {'a leap year' if is_leap else 'not a leap year'}")

if __name__ == "__main__":
    main()

# Question 2

import math

nums = input()
values = list(map(float, nums.split()))   
#print(values)

total = sum(values)
#print(total)

floor_sum = math.floor(total)
ceil_sum = math.ceil(total)
round_sum = round(total)

floor_ceil_diff = floor_sum - ceil_sum
ceil_round_diff = ceil_sum - round_sum
floor_round_diff = floor_sum - round_sum

print(float(floor_ceil_diff))
print(float(ceil_round_diff))
print(float(floor_round_diff))