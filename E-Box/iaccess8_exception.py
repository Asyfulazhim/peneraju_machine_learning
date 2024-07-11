#Problem 1
numlist = [2,3,1,5,6,7,1]
print(numlist)
n = int(input("Enter n\n"))

try:
    numlist[n-1]

except IndexError:
    print("Index Value out of range")

else:
    sum = 0
    for i in range(n):
        sum += numlist[i]

    print(f"Sum = {sum}")

# Problem 2
class CustomError(Exception):
    pass

def validatepassword(password):
    if not (any(char.islower() for char in password) and 
            any(char.isupper() for char in password) and 
            any(char.isdigit() for char in password)):
        raise CustomError("Invalid Password Exception")

username = input("Enter the username\n")
password = input("Enter the password\n")

try:
    validatepassword(password)
except CustomError as e:
    print("CustomException:",e)
else:
    print(f"Employee Username: {username}")
    print(f"Password: {password}")