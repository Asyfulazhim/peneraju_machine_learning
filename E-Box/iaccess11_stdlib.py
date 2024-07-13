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

# Get the input list of numbers
numbers = list(map(float, input().split()))

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Calculate the floor, ceil, and round of the sum
floor_sum = math.floor(total_sum)
ceil_sum = math.ceil(total_sum)
round_sum = round(total_sum)

# Calculate the differences
diff1 = floor_sum - ceil_sum
diff2 = ceil_sum - round_sum
diff3 = floor_sum - round_sum

# Print the results
print(f"{diff1:.1f}")
print(f"{diff2:.1f}")
print(f"{diff3:.1f}")