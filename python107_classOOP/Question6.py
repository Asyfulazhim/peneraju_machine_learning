'''
Problem 6

Write a Python class that has two methods: getString and printString , 
The getString accept a string from the user and printString prints the string in upper case.
'''

class Print:
    def getString(self):
        self.s = input("Enter a string:")
    def printString(self):
        print(self.s.upper())

s = Print()
s.getString()
s.printString()

    
