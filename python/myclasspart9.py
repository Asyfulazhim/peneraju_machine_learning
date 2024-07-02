

class Calculator:
    # this method can also be called as instance method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
mycalculator = Calculator(10,20)
print(mycalculator.add())