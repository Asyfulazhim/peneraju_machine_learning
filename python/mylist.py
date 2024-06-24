fruits = ["Apple", "Orange", "mango", "BAnana", "grapes"]
print(fruits)

# Modifiable
fruits.append("durian")
print(fruits)

#insert item inside existing list
fruits.insert(1, "rambutan")
print(fruits)
fruits.insert(3, "cempedak")
print(fruits)
fruits.insert(5, "dummy")
print(fruits)

#update items in the list
fruits[5] = "Mangosteen"
print(fruits)

# remove item in list
fruits.remove("durian")
print(fruits)

# remove the last item
fruits.pop()
print(fruits)

# delete an item by index
del fruits[3]
print(fruits)

# remove all item in list
fruits.clear()
print(fruits)

# delete entire list
del fruits
# print(fruits) # error because fruits is deleted
fruits = ["apple", "mango","Orange", "mango", "apple","banana", "grapes", "apple"]
print(fruits.index("mango"))

# get index second mango
print(fruits.index("mango", 2))
# or
newfruits = fruits[2:] #0,1
print(newfruits.index("mango")+1)

# enumerate is an iterable object
print(list(enumerate(fruits)))

# use for loop
for fruit in enumerate(fruits):
    #print(fruit[0])
    #print(fruit[1])
    # use if
    if fruit[1] == "mango":
        #print the position
        print("Mango is in position: ", fruit[0])

# how many apples in the list
print("Number of apples: ",fruits.count("apple"))

# how many mango in the list
print("Number of mango: ",fruits.count("mango"))
# sort the list
fruits.sort()
print(fruits)
# sort the list in reverse order
fruits.sort(reverse=True)
print(fruits)
print('='*40)

# demonstrate shallow copy
x = [10,20,30,40,50]
y = x
print(x)
print(y)

x[3] = 35
print(x)
print(y)
print('='*40)

# perform deep 
# 1st solution
x = [10,20,30,40,50]
y = x.copy()
print(x)
print(y)
x[3] = 35
print(x)
print(y)
print('='*40)

# 2nd solution
x = [10,20,30,40,50]
y = []
for i in x:
    y.append(i)
print(x)
print(y)
x[3] = 35
print(x)
print(y)
print('='*40)

# fruits is an instance of list class
# class always return something
x = list([10,20,30,40,50])
print(x)
print(type(x))
print('='*40)

# in python to invoke or call, we use ()
# () is used ib ecpression
# to call built in function print() sum() id()
# to create object we call class type() int() float()
# to call method sort() append() insert() split()
# to call function inside a module sys.path ()

