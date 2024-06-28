
# class is a blue print
# which contain variables and function
class Student:

    def __init__(self):
        print("Object is created")
    
    def attendClass(self):
        print("Attending Class")
    
    def doProject(self, projectname):
        print("Doing Project: ", projectname)
    
    def attendExam(self,exam):
        grade = "A"
        print("Attending Exam: ", exam, "Grade: ", grade)
    
zul = Student()
zul.attendClass()
zul.doProject("Project 1")
zul.attendExam("Pyhton103")
