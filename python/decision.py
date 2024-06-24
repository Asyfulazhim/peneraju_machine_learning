# Write a program to find whether the given number is positive, negative or zero
# Write a program to find whether our business is making profit, loss or breakeven

expenses = 1000
sales = 1100

# Objective 1: Just say whether we are making profit (single condition)
# if (sales - expenses > 0)
if (sales > expenses):
    # block of code
    print("You are making Profit")
    print("Good Lah")

# Objective 2: Say whether we are making profit or loss (2 conditions)
if (sales > expenses):
    print("You are making Profit")
else:
    print("You are making Losses")

# Objective 3: Say whether we are making profit or loss or breakeven (3 conditions)
if (sales > expenses):
    print("You are making Profit")
else:
    if (sales == expenses):
        print("You are making breakeven")
    else:
        print("You are making Losses")

if (sales > expenses):
    print("You are making Profit")
elif (sales == expenses):
    print("You are making breakeven")
else:
    print("You are making Losses")


print("Thank You")

# if the statement to be executed is not a block of code
# it is a single statement then we can write the if and statement
# in the same line

# find whether the given number is even
givennumber = 5
if (givennumber % 2 == 0): print("Even Number")

# find whether the given number is even or odd
print("Even Number") if (givennumber % 2 == 0) else print("Odd Number")

givennumber = 1
# find whether the given number is positive, negative or zero
print("+ve") if (givennumber > 0) else print("-ve") if (givennumber < 0) else print("zero")