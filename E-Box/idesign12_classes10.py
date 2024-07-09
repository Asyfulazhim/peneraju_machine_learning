
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old and her email id is {self.first_name}.{self.last_name}@gmail.com"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


#from Person import Person

person_first_name = input("Enter first name\n")
person_last_name = input("Enter last name\n")
person_age = input("Enter age\n")
person = Person(person_first_name, person_last_name, person_age)
print("Full name of the person is ",person.fullname())
print("Person Details")
print(person)
	
