class Passport:

    def __init__(self, country, passportnumber):
        self.country = country
        self.passportnumber = passportnumber

    def __str__(self):
        return f"Country: {self.country}\nPassport Number: {self.passportnumber}"



class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        # Customer has a passport
        # When you have a relationship with custo
        # It become the property 
        self.passport = None
    
    def __str__(self):
        message = f"First: {self.firstname}\n"
        message += f"Last Name: {self.lastname}\n"
        message += f"IC Number: {self.icnumber}\n"
        if (self.passport != None):
            message += f"Passport: {self.passport}\n"

        return message

peter = Customer("Parker", "Peter")
passport = Passport("UK", "E023491")
peter.passport = passport
print(peter)
# noe we know how to convert a python object to a dictionary
print(peter.__dict__)
