while True:
    try:
        x = int(input("Enter a positive integer\n"))

        if x <=0:
            raise ValueError
        else:
            print(f"Good! You entered {x}")
            break

    except ValueError:
        print("You entered a negative number. Retry!")