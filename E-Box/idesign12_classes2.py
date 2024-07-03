'''
class Person:
	def __init__(self,name, age):
		self.__name = name
		self.__age = age
	
	def from_string(cls, person_str):
		name, age = person_str.split(",")
		return cls(name, int(age))
		
	def __str__(self):
		#fill your code
		return f"{self.__name} is {self.__age} years old"

print("Creating object using __init__ method")
person_name = input("Enter name\n")
person_age = input("Enter age\n")
person1 = Person(person_name, person_age)
print("Person Details")
print(person1)
print("\n")

print("Creating object using class method")
person_str = input("Enter name and age in comma separated format\n")
person2 = Person.from_string(person_str)
print("Person Details")
print(person2)
'''

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split(",")
        return cls(name, int(age))

    def __str__(self):
        return f"{self.__name} is {self.__age} years old"

print("Creating object using __init__ method")
person_name = input("Enter name\n")
person_age = input("Enter age\n")
person1 = Person(person_name, person_age)
print("Person Details")
print(person1)
print("\n")

print("Creating object using class method")
person_str = input("Enter name and age in comma separated format\n")
person2 = Person.from_string(person_str)
print("Person Details")
print(person2)