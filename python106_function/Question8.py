# Problem 8
# Write a python function that takes variable length parameters and returns 
# maximum and minimum number in the parameter numbers.
# For example if we call the function: maximumMinimum(10, 20, 30, 40, 50)
# The function must return: [10, 50]
def maximumMinimum(*numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
            if number < minimum:
                minimum = number
    return [minimum, maximum]

# call function
print(maximumMinimum(10, 20, 30, 40, 50))

            

