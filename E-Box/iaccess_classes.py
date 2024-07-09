# Question 1
class Shape:
    def __init__(self):
        pass
    
    def display_parameters(self):
        pass

class CalAreaSquare(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def display_parameters(self):
        print(f"Length of Square : {self.side}")
    
    def area(self):
        return self.side ** 2

class CalAreaRectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def display_parameters(self):
        print(f"Length of Rectangle : {self.length}")
        print(f"Breadth of Rectangle : {self.width}")
    
    def area(self):
        return self.length * self.width

class CalAreaTriangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
    
    def display_parameters(self):
        print(f"Base of Triangle : {self.base}")
        print(f"Height of Triangle : {self.height}")
    
    def area(self):
        return 0.5 * self.base * self.height

class CalAreaCircle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def display_parameters(self):
        print(f"Radius of Circle : {self.radius}")
    
    def area(self):
        return 3.14 * (self.radius ** 2)

def main():
    print("Select an Option")
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")
    
    option = int(input())
    
    if option == 1:
        side = int(input("Enter the length\n"))
        square = CalAreaSquare(side)
        square.display_parameters()
        print(f"Area of Square : {square.area()}")
    elif option == 2:
        length = int(input("Enter the length\n"))
        width = int(input("Enter the breadth\n"))
        rectangle = CalAreaRectangle(length, width)
        rectangle.display_parameters()
        print(f"Area of Rectangle : {rectangle.area()}")
    elif option == 3:
        base = int(input("Enter the base\n"))
        height = int(input("Enter the height\n"))
        triangle = CalAreaTriangle(base, height)
        triangle.display_parameters()
        print(f"Area of Triangle : {triangle.area():.2f}")
    elif option == 4:
        radius = int(input("Enter the radius\n"))
        circle = CalAreaCircle(radius)
        circle.display_parameters()
        print(f"Area of Circle : {circle.area():.2f}")
    else:
        print("Invalid option. Please enter a valid choice (1/2/3/4).")

if __name__ == "__main__":
    main()
    
# Question 2
'''
Create a base class named Student with the following  member variables / attributes  .

Include a 4-argument constructor. The order of parameters passed 
to the constructor is id,name,department,courseId.
Override a str() method to display the details of the class.

Create a child class named StudentRating with the following  member variables / attributes

Include a 4-argument constructor. The order of parameters passed to the constructor is 
id,review, stars, student(inherited from Student class.
Override a str() method to display the details of the class.

Input and Output Format:  
Refer sample input and output for formatting specifications.  
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output:
Enter the student id
12
Enter the student name
Prakash
Enter the department
ECE
Enter the course id
250
Enter the Rating id
4
Enter review
Very good Student!!!
Enter number of stars
5
Student :
Id :  12
Name :  Prakash
Department :  ECE
Course Id :  250
Rating ID :  4
Review :  Very good Student!!!
Rating Stars :  5
'''
class Student:
    def __init__(self, id, name, department, courseId):
        self.id = id
        self.name = name
        self.department = department
        self.course_id = courseId
    def __str__(self):
        return f"Student :\nId : {self.id}\nName : {self.name}\nDepartment : {self.department}\nCourse Id : {self.course_id}"
    
class StudentRating(Student):
    def __init__(self, ratingId, review, stars, student):
        super().__init__(student.id, student.name, student.department, student.course_id)
        self.ratingId = ratingId
        self.review = review
        self.stars = stars
    def __str__(self):
        return f"{super().__str__()}\nRating ID : {self.ratingId}\nReview : {self.review}\nRating Stars : {self.stars}"

# Input
print("Enter the student id")
id = int(input())
print("Enter the student name")
name = input()
print("Enter the department")
department = input()
print("Enter the course id")
course_id = int(input())
print("Enter the Rating id")
rating_id = int(input())
print("Enter review")
review = input()
print("Enter number of stars")
stars = int(input())  

# Create Student object
student = Student(id, name, department, course_id)

# Create StudentRating object
student_rating = StudentRating(rating_id, review, stars, student)

# Print StudentRating details
print(student_rating)