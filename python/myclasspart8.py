# in every class there will be many properties
# and very few properties are common to all the object
# better keep the property in class level than object level

class Participant:
    # class level property
    course = "Python Data Science / Machine Learning"

    def __init__(self, firstname, lastname):
        
        self.firstname = firstname
        self.lastname = lastname
        count = 1
        print(self.firstname, self.lastname, count)
    
    def getFullName(self):
        print(self.firstname, self.lastname)


Khairi = Participant("Khairi", "Abu Bakar")
