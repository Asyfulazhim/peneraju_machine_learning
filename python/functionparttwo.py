# function can have inner fucntion
def sum(a,b):
    return a+b

x = 10

def authenticate(username, password):
    def calculateSI(principle, period, rate):
        result = (principle * period * rate) / 100
        return result
    if (username == "admin" and password == "pwd123"):
        return calculateSI

authenticate("admin", "pwd123")

# calculateSI(1000,1,6)
# this will throw error because calculateSI is inner function of authenticate function
# however if the outer function return the inner function
# we can call inner function
func = authenticate("admin", "pwd123")
print("Simple Interest:", func(1000,1,6))
print("Simple Interest:", authenticate("admin", "pwd123")(1000,1,6))

# anonymous function mean function without name
# how to call them?
# lambda function is anonymous function
# sum = def (a, b):
#         return a+b
# the above is not a valid syntax in python, however this is every function are
# handled by python itself
# that means in pytho every function is an anonymous function

# lambda function allow us to create function in one line
# add = def(a,b): return
# using lambda does not require () and return keyword
add = lambda a, b: a+b
'''
# normal def
fahrenheitvalues = [32, 212, 100, 212, 90, 0]
def fahrenheitToCelcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celciusvalues = list(map(fahrenheitToCelcius, fahrenheitvalues))

# using lambda
celciusvalues = map(lambda fahrenheit:  (fahrenheitvalues - 32) * 5/9,)
print(list(celciusvalues))
'''
# normal def
fahrenheitvalues = [32, 212, 100, 212, 90, 0]
def fahrenheitToCelcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celciusvalues = list(map(fahrenheitToCelcius, fahrenheitvalues))
print(celciusvalues)

# using lambda
fahrenheitvalues = [32, 212, 100, 212, 90, 0]
celciusvalues = list(map(lambda fahrenheit: (fahrenheit - 32) * 5/9, fahrenheitvalues))
print(celciusvalues)