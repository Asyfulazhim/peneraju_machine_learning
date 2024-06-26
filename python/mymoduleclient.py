# First Module
# import mymodule

# print(mymodule.simpleInterest(1000,1,6))

# Second Method
# python recommend this method
from mymodule import simpleInterest, compoundInterest
print(simpleInterest(1000,1,6))
print(compoundInterest(1000,1,6))
print("-"* 30)

#Third method
from mymodule import *
print(simpleInterest(1000,1,6))
print(compoundInterest(1000,1,6))
print("-"* 30)