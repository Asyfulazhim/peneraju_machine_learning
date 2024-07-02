# Syntax Error
# x=1
# if(x==1):
# print("x is 1")

# Logical Error
# program is running but output is not as expected

# Runtime Error
# error data from the user or system
principle = int(input("Principle: "))
period = int(input("Period"))
rate = int(input("Rate: "))
Interest = (principle * period * rate)/100
print("Simple Interest: ", Interest)

# how to solve runtime error?
try:
    principle = int(input("Principle: "))
    period = int(input("Period"))
    rate = int(input("Rate: "))
    Interest = (principle * period * rate)/100
    print("Simple Interest: ", Interest)
except:
    print("Invalid Input")
