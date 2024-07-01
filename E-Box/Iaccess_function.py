'''
Write a program to multiple two values using default arguments.
Suppose the 2 input values are a and b.

Make 3 function calls as follows:
1) multiply(a)
2) multiply(a,b)
3) multiply(a,b=9)

Functional Specifications:
def multiply(argument1,argument2=10):

Input Format:
Input consists of 2 integers.

Output Format:
Output prints the product of the given input.
 
Sample Input  and Output:

5
3
The result is 50
The result is 15
The result is 45
'''
def multiply(a,b=9):
    return a*b

a=int(input())
b=int(input())
print("The result is",multiply(a))
print("The result is",multiply(a,b))
print("The result is",multiply(a,b=9))


'''
Displaying user inputs using multiple return values
Write a program to display the user entered details and return multiple values.
Functions Sepcifications:
def multiVarFunc()

Input Format:
First line of input consists of String which is department name.
Second line of input consists of integer input which is the total number of students
Third line of input consists of integer input which is the total number of faculty.

Output Format:
Display the user inputs.

Sample Input and Output:
Enter department name:
CSE
Enter the number of total students:
60
Enter the number of total faculties:
15
Details:
Department:CSE
Total students:60
Total faculties:15
'''

def multiVarFunc(department,total_students,total_faculties):
    print(f"Details:\nDepartment:{department}\nTotal students:{total_students}\nTotal faculties:{total_faculties}")

def main():
    department=input("Enter department name:\n")
    total_students=int(input("Enter the number of total students:\n"))
    total_faculties=int(input("Enter the number of total faculties:\n"))
    multiVarFunc(department, total_students, total_faculties)

if __name__ == "__main__":
    main()

