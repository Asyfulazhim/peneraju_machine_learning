

class Calculator:
    # this method can also be called as instance method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
mycalculator = Calculator(10,20)
print(mycalculator.add())

class Utility:
    def addition(x, y):
        return x + y
    
    def subtraction(x, y):
        return x - y
    
print(Utility.addition(100,200))

class Customer:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def getFullname(first, last):
        return first + last
    
    def __str__(self):
        return Customer.getFullname(self.first, self.last)
    
myCustomer = Customer("John","David")
print(myCustomer)
