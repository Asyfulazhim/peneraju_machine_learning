c = input("Enter characters:")
char = list(c)
charlength = len(char)

i = 0
while i < charlength:
    count = 1
    while i + 1 < charlength and char[i] == char[i+1]:
        i += 1
        count += 1
    print(f"{char[i]}{count}", end="")
    i += 1