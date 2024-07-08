try:
    try:
        n = int(input("Enter the number of matches\n"))
    except EOFError:
        print("Type Error Exception")
        exit()

    total = 0
    print("Enter the scores")

    for _ in range(n):
        while True:
            try:
                m = int(input())
                total += m
                break
            #except ValueError:
               # print("Invalid input. Please enter a valid score.")
            except EOFError:
                print("Type Error Exception")
                exit()

    avg = total / n
    print(f"Batting average: {avg:.2f}")

except ValueError:
    print("Type Error Exception")