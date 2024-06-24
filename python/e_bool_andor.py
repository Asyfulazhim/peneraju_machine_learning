'''
age = int(input("enter your age: "))
can_learn_pr = age >= 10 and age < 70
usually_working = age >=23 and age<70

print(f"You can learn programming: {can_learn_pr}")
print(f"At age {age}, you are usually working: {usually_working}")

print(bool(32))
print(bool("asy"))

print(bool(0))
print(bool(""))

x = 0 or 34
print(x)


name = input("Enter your name: ")
surname = input("Enter your surname: ")

greeting = name or f"Mr. {surname}"
print(greeting)
'''

print(not 35)