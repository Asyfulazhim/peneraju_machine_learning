
def addition(n1,n2):
    return n1 + n2

def subtraction(n1,n2):
    return n1 - n2

def multiplication(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

def modulus(n1,n2):
    return n1 % n2

def main():
    print("Select the operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulus")
    print("Enter the choice(1/2/3/4/5):")

    choice=int(input())
    if choice > 5:
        print("Invalid Input")
    else:
        n1=int(input("Enter the first number\n"))
        n2=int(input("Enter the second number\n"))
        if choice==1:
            print(f"{n1} + {n2} = {addition(n1,n2)}")
        elif choice==2:
            print(f"{n1} - {n2} = {subtraction(n1,n2)}")
        elif choice==3:
            print(f"{n1} * {n2} = {multiplication(n1,n2)}")
        elif choice==4:
            print(f"{n1} / {n2} = {division(n1,n2)}")
        else: 
            print(f"{n1} % {n2} = {modulus(n1,n2)}")
        

    
 
if __name__ == "__main__":
    main()
