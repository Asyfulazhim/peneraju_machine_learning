class User:
    def __init__(self,name,username,password,mobile_number):
        self.name = name
        self.username = username
        self.password = password
        self.mobile_number = mobile_number

    def __eq__(self,obj):
        return self.mobile_number == obj.mobile_number
    

# from User import User

print("Enter the details of User 1")
name_1 = input("Name :\n")
username_1 = input("Username :\n")
pwd_1 = input("Password :\n")
mobile_number_1 = input("Mobile Number :\n")

print("Enter the details of User 2")
name_2 = input("Name :\n")
username_2 = input("Username :\n")
pwd_2 = input("Password :\n")
mobile_number_2 = input("Mobile Number :\n")

#Fill your code here
user_1 = User(name_1,username_1,pwd_1,mobile_number_1)
user_2 = User(name_2,username_2,pwd_2,mobile_number_2)

if user_1 == user_2:
    print("User 1 and User 2 are equal")
else:
    print("User 1 and User 2 are not equal")