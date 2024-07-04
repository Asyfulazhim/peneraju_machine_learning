def sum_of_integers():
    try:
        with open("sample.txt", "r") as file:
            integers = [int(line.strip()) for line in file]
            total_sum = sum(integers)
            print(f"The sum of the integers in the file sample.txt is: {total_sum}")
    except FileNotFoundError:
        print("The file sample.txt does not exist.")
    except ValueError:
        print("The file sample.txt contains non-integer values.")

sum_of_integers()