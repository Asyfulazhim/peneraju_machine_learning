# So can u please help to write a program to find the second largest number of union set.input and output format specifications are shown below.

# Input Format Specifications:

# The first line of input consists of several sets you required.
# The second-line consists of entering the inputs to the sets.
# Note that print the elements in sorted order.

# Output Format Specifications:

# The first line of output contains the Union of all sets.
# The second line of output contains the Second largest Number of Union sets.
# Sample Input 1:
# 3
# 1,1
# 2,1
# 4,5
# Sample Output 1:
# set([1, 2, 4, 5])
# 4

n = int(input())

unique_list = []
for _ in range(n):
    a, *b = map(int, input().split(','))
    unique_list.extend([a, *b])

unique_list = list(set(unique_list))  # Convert set to list
unique_list.sort()
print(f"set({unique_list})")
print(unique_list[-2])