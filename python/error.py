x = 11

# Syntax Error
# if (x % 2 == 0):
# print("Even Number")

# Logical Error
# if (x % 2 == 0):
#    print(f"Given Number is {x}")
# print("Even Number")

# Runtime Error

try:
    # we know the following line is taking user input
    # in future this may throw error
    # then you must place this code inside a block called
    # try except
    principle = int(input("Principle: "))
except ValueError:
    # when that error occur what we must do
    print("Principle amount must be an Integer")

except Exception as e:
    print("Something went wrong:", e)

else:
    print("All is well")

finally:
    print("Xie xie")

# The program does not get terminated abnormally


period = int(input("Period: "))
rate = int(input("Rate: "))
interest = (principle * period * rate) / 100
print("Interest Amount: ", interest)