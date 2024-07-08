class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 18:
        raise CustomError("CustomException: InvalidAgeRangeException")
def main():
    name = input("Enter the Name\n")
    age = int(input("Enter the age\n"))
    try:
        validate_age(age)
        print(f"Voter name: {name}")
        print(f"Voter age: {age}")
    except CustomError as e:
        print(e)

if __name__ == "__main__":
    main()