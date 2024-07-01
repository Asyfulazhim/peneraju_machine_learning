# Is - A Relationship
# Alimni is a student

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""

# Alumni extends Student class
class Alumni(Student):

    def __init__(self,firstname, lastname, alumninumber):
        # static calling the __init__ 
        # Student.__init__(self,firstname, lastname)
        # you can use the keyword "super"
        super().__init__(firstname,lastname)
        self.alumninumber = alumninumber
        pass

    def __str__(self):
        return f"First Name: {self.firstname} \
        \nLast Name: {self.lastname} \
        \nIC Number: {self.icnumber} \
        \nAlumni Number: {self.alumninumber}"
    

alumni = Alumni("Parker", "Fikri", 970856)
#alumni = Alumni("","")
print(alumni)