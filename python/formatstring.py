'''
number = 5
name = 'SuiSyahmi'
print(f"the name is: {name} and the number is {number}")
'''
name = "David"
batch = 101
fee = 1344245.67889
inputstring = "Hello " + name + " welcome to python class " + str(batch)
print(inputstring)

# how much space is required
inputstring = f"Hello {name:40s}, welcome to python class {batch}"
print(inputstring)

# put name to center
inputstring = f"Hello {name:^40s}, welcome to python class {batch}"
print(inputstring)

# put name to right
inputstring = f"Hello {name:>40s}, welcome to python class {batch}"
print(inputstring)

# put name to right
inputstring = f"Hello {name:*>40s}, welcome to python class {batch}"
print(inputstring)

# trucate to 3 character
inputstring = f"Hello {name:.3}, welcome to python class {batch}"
print(inputstring)

# focus on decimal, take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d}"
print(inputstring)

# focus on decimal, take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL for RM{fee:10.2f}"
print(inputstring)

# focus on decimal, take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL for RM{fee:.2f}"
print(inputstring)

# focus on decimal, take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL for RM{fee:,.2f}"
print(inputstring)

#binary --> fee:.2b
#Octagon --> fee:.o
#hexagon --> fee:.x