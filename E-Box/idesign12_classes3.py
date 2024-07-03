class Address:
	def __init__(self, street, city, state):
		self.__street = street
		self.__city = city
		self.__state = state
	
	def __str__(self):
		return f"{self.__street}, {self.__city}, {self.__state}"


class Person:
	def __init__(self, name, age, address):
		self.__name = name
		self.__age = age
		self.__address = address
	
	def __str__(self):
		return f"{self.__name} is a person who is {self.__age} years old and lives in the following address : {self.__address}"


def main():
	person_name = input("Enter name\n")
	person_age = input("Enter age\n")
	print("Enter address")
	street = input("Enter street\n")
	city = input("Enter city\n")
	state = input("Enter state\n")
	person_address = Address(street,city,state)
	person = Person(person_name, person_age,person_address)
	print("Person Details")
	print(person)


if __name__ == "__main__":
	main()