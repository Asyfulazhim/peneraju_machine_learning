# function can have inner fucntion
def sum(a,b):
    return a+b

x = 10

def authenticate(username, password):
    def calculateSI(principle, period, rate):
        result = (principle * period, rate) / 100
        return result
    if (username == "admin" and password == "pwd123"):
        print("Simple Interest:", calculateSI(1000,1,6))
        pass

authenticate("admin", "pwd123")

# calculateSI(1000,1,6)
# this will throw error because calculateSI is inner function of authenticate function
