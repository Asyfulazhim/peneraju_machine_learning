# Problem 9
# Write a simple Python function that takes a number(n) as a parameter. 
# Then the function prints out the first n rows of Pascal's triangle. 
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

def Pascal(n) :
    pascal = {}
    for line in range(0, n) :
        listinrow = []
        for i in range(0, line + 1) :
            listinrow.append(str(binomialCoeff(line,i)))
        pascal[line] = listinrow
    Pascal_Dict_to_List(pascal)
    
def Pascal_Dict_to_List(list):
    for i in range(0, len(list)):
        ListToString(list[i])
        
def ListToString(list):
    width = 40
    my_string = ' '.join(list)
    padding = " " * ((width - len(my_string)) // 2)
    print(f"{padding}{my_string}{padding}")
   
    
def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
    return res

n = 7
Pascal(n)


# This code is contributed by Nikita Tiwari.


# def print_centered(s, width=40):
#     """Print a string at the center of the console"""
#     padding = " " * ((width - len(s)) // 2)
#     print(f"{padding}{s}{padding}")

# # Example usage:
# print_centered("Perfect Numbers:")
# print_centered("3, 6, 28, 496")