# Multiple Inheritance

class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Card doSomething()")

class ATMCard(Card):
    def __init__(self):
        pass
    # def doSomething(self):
    #     print("ATM Card doSomething()")

class CreditCard(Card):
    def __init__(self):
        pass
    # def doSomething(self):
    #     print("Credit Card doSomething()")
        
class DebitCard(Card):
    def __init__(self):
        pass
    # def doSomething(self):
    #     print("Debit Card doSomething()")

class BankCard(ATMCard, CreditCard, DebitCard):
    def __init__(self):
        pass
    def doSomething(self):
        #print("Bank Card doSomething()")
        super().doSomething()

bankCard = BankCard()
bankCard.doSomething()

# Method Resolution Order
print(BankCard.__mro__)
# <class '__main__.BankCard'>, 
# <class '__main__.ATMCard'>, 
# <class '__main__.CreditCard'>, 
# <class '__main__.DebitCard'>, 
# <class '__main__.Card'>, 
# <class 'object'>

# BIGGEST CONCLUSION:
# Every class in python is inherited from a class called object
# class object:
#   def __init__():
#       pass
#   def __str__():
#       print(memory address)

class Student:
    # def __str__(self):
    #     return "Student"
        pass
class Alumni(Student):
    # def __str__(self):
    #     return "Alumni"
    pass
    
alumni = Alumni()
print(alumni)

# Iterator object like enumeratoe, range, map, filter do not override
# __str__ method. They override __repr__ method.