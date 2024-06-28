
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
    
zul = Student("Ahmad", "Syahmi", "00077667412")
zul.attendClass()
zul.doProject("Project 1")
zul.attendExam("Pyhton103")
