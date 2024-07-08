'''
Create a class named Student with a single attribute – marks.
Include a method named check_marks in the Student Class.
This method checks whether the marks is greater than  or equal to 90 and if it is greater than or equal to 90, the method returns True.
If the marks is less than 90, a custom Exception named NotEligibleException is raised and an appropriate message as shown in the sample output is displayed.


Create a custom Exception class named NotEligibleException.

 
Create an object of the student class and test the above methods.
'''
class NotEligibleException(Exception):  # Inherit from Exception
    def __str__(self):
        return "Inside Except Block : Not Eligible"

class Student:
    def __init__ (self, marks):
        self.marks = marks

    def check_marks(self):
        if self.marks >= 90:
            return True
        else:
            raise NotEligibleException ()

mark = Student(int(input("Enter marks of student\n")))

try:
    if mark.check_marks():  # Call the method with parentheses
        print("Eligible")

except NotEligibleException as e:
    print(e)