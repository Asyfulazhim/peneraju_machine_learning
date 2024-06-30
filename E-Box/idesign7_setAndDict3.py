# Input and Output format:
# The first line contains the integer, which indicates the number of students, 'n'.
# The next 'n' lines contain the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed to find the average mark of him.
# The output is the average of the marks obtained by the particular student correct to 2 decimal places.

# Note: Use Dictionary concept to solve the problem.
# Sample Input 1:
# 4
# aaa 35 67 89
# bbb 45 46 48
# ccc 78 78 78
# ddd 78 90 89
# ddd
# Sample Output 1:
# Average Mark of is : 85.67
 

# Sample Input 2:
# 3
# aaa 46 78 89
# bbb 34 68 90
# ccc 13 56 34
# ccc
# Sample Output 2:
# Average Mark of is : 34.33

def update_dict(n,dict):
    name, *marks = n.split()
    dict[name] = [int(mark) for mark in marks]

def calculate_avg(key,dict):
    marks = dict[key]
    avg = sum(marks)/len(marks)
    print(f"Average Mark of {key} is : {avg:.2f}")

def main(m):
    dict = {}
    for i in range(m):
        name = input()
        update_dict(name, dict)
    key = input()
    calculate_avg(key,dict)

n = int(input())
main(n)
