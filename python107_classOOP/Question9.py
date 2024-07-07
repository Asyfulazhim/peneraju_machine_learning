'''
Write a Python class BankAccount with attributes like accountNumber, 
openingBalance, currentBalance dateOfOpening and customerName. 
Add methods like deposit, withdraw, and checkBalance
'''

class BankAccount:
    def __init__(self, accountNumber, openingBalance, currentBalance, dateOfOpening, customerName):
        self.accountNumber = accountNumber
        self.openingBalance = float (openingBalance)
        self.currentBalance = float (currentBalance)
        self.dateOfOpening = dateOfOpening
        self.customerName = customerName

    def deposit(self,depo):
        self.currentBalance += depo
        print(self.currentBalance)

    def withdraw(self, draw):
        self.currentBalance -= draw
        print(self.currentBalance)

    def checkBalance(self):
        print(self.currentBalance)

p1 = BankAccount("1234567890", "5000.00", "5000.00", "2024-07-07", "John")
p1.deposit(3000)
p1.withdraw(300)
p1.checkBalance()


