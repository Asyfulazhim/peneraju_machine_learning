
class Student:

    def __init__(self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.program = ""
        self.address = ""
    
    def attendClass(self):
        print("Attending Class")
    
    def doProject(self, projectname):
        print("Doing Project: ", projectname)
    
    def attendExam(self,exam):
        grade = "A"
        print(f"Attending Exam: {exam},\nGrade: {grade}")
    
    def info(self):
        print("First name:", self.firstname)
        print("Last name:", self.lastname)
        print("IC Number:", self.icnumber)
        print("Program:", self.program)
        print("Address:")
        print(self.address["Street"])
        print(self.address["City"])
        print(self.address["State"])
                                                                    
    
zul = Student("Ahmad", "Syahmi", "00077667412")
zul.attendClass()
zul.doProject("Project 1")
zul.attendExam("Pyhton103")
zul.address = {
    "Street": "15 Jalan s32",
    "City": "Kuala Lumpur",
    "State": "Selangor"
    }
zul.info()

# how we can set value for the properties
# 1) using constructor (__init__method)
# 2) you can set value to the property directly using dot operator
# eg: zul.program["Python", "Data Science", "Machine Learning"]

