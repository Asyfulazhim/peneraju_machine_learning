# Question 1
# class Shape:
#     def __init__(self):
#         pass

#     def area(self):
#         pass


# class CalAreaSquare(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         area = self.side * self.side
#         print(f"Area of Square : {area}")


# class CalAreaRectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         area = self.length * self.breadth
#         print(f"Area of Rectangle : {area}")


# class CalAreaTriangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         area = 0.5 * self.base * self.height
#         print(f"Area of Triangle : {area:.2f}")


# class CalAreaCircle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         area = 3.14 * self.radius * self.radius
#         print(f"Area of Circle : {area:.2f}")


# print("Select an Option")
# print("1.Square")
# print("2.Rectangle")
# print("3.Triangle")
# print("4.Circle")
# n = int(input())
# if n == 1:
#     print("Enter the side")
#     side = int(input())
#     print(f"Side of square : {side}")
#     s = CalAreaSquare(side)
#     s.area()
# elif n == 2:
#     print("Enter the length")
#     length = int(input())
#     print("Enter the breadth")
#     breadth = int(input())
#     print(f"Length of Rectangle : {length}")
#     print(f"Breadth of Rectangle : {breadth}")
#     r = CalAreaRectangle(length, breadth)
#     r.area()
# elif n == 3:
#     print("Enter the base")
#     base = int(input())
#     print("Enter the height")
#     height = int(input())
#     print(f"Base of Triangle : {base}")
#     print(f"Height of Triangle : {height}")
#     t = CalAreaTriangle(base, height)
#     t.area()
# elif n == 4:
#     print("Enter the radius")
#     radius = int(input())
#     print(f"Radius of Circle : {radius}")
#     c = CalAreaCircle(radius)
#     c.area()

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