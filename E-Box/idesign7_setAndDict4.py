# You have a record of students. Each record contains the student's name 
# and their marks in Maths, Physics, Chemistry, and computer science. 
# The marks can be floating values. 
# The user enters some integer followed by the names and marks of students. 
# You are required to save the record in a dictionary data type. 
# The user then enters a student's name. 
# The output is the second-highest mark obtained by that student.

# Input format:
# The first line contains the integer, which indicates the number of students, 'n'.
# The next 'n' lines contain the name and marks obtained by that student separated by a space.
# The final line contains the name of a particular student to find the second-highest mark of him.

# Output format:
# The output is the second-highest mark obtained by the particular student. If he scored the same marks in all subjects, then print a message as shown sample I/O.
# If the student name does not exist then print  "Student doesn't exist". [Refer Sample I/O]

# Sample Input 1:
# 4
# Sandy 78 67 89 100
# John 45 46 48 23
# Cherry 78 78 78 78
# Ratan 78 90 89 56
# Sandy
# Sample Output 1:
# Second Highest mark of Sandy: 89

def update_dict(n,dict):
    name, *marks = n.split()
    dict[name] = [int(mark) for mark in marks]

def second_highest(key,dict):
    marks = dict[key]
    for mark in marks:
        if sum(marks)//len(marks) == mark:
            print(f"{key} scored same marks in all subjects: {mark}")
            break
        elif mark == max(marks):
            marks.remove(mark)
        print(f"Second Highest mark of {key}: {max(marks)}")
        break

def main(m):
    dict = {}
    for i in range(m):
        name = input()
        update_dict(name, dict)
    key = input()
    if key in dict:
        second_highest(key,dict)
    else:   
        print("Student doesn't exist")
n = int(input())
main(n)