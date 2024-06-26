# Write a python function that takes a number as parameter 
# and prints the multiplication table of that number

n = int(input("Enter integer:"))
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

multiplication_table(n)
