def add(a,b):
    result = a + b
    return result

# print(result)

x = 10

def printx():
    print(x)
printx()
print(x)

#to check whether x value in global context is also modified or not. 
def modifyx():
    x = 15
    print(x)

modifyx()
print(x)

# here x value in global context is not modified 
# because in modifyx() function, x is treated

# if really want to modify the variable in the global context
# then the fx must return the value

def traditionalModify():
    x = 15
    return x
x = traditionalModify()
print(x)
# this is the best practice

# however, there is shortcut in python
# because if using traditional, only return sigle value
# which mean we can only modify only 1 value
# how if i want to modify multiple value
# then we can use global keyword

def pythonModify():
    global x
    x = 25
    print("Inside fx (pythonModify)", x)
pythonModify()
print(x)

# let discuss about scope of variable in function context
def simpleInterest(principle, period, rate):
    result = 0
    def printSimpleInterest():
        temp = 0
        print("Simple Interest:", result)
    # print(temp) #not allowed
    result = (principle * period * rate)/100
    printSimpleInterest()  
simpleInterest(1000,1,6)
#print("Interest Amount: ",result)