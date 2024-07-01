# Is - A Relationship
# Alimni is a student

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""

# Alumni extends Student class
class Alumni(Student):
    pass

alumni = Alumni("Parker", "Fikri")
