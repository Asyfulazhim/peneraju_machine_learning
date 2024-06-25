# Problem 4
# Get number of items as input and generate that many Armstrong Numbers

n = int(input ("enter any number:" ))
armstrongNumber = 0
for a0 in range(1,100000):
  for i in range(1, 6):
    if a0 // (10**i) == 0:
        digit = i
        break

  if(a0 // 100000 != 0):
    print(a0, "is over the limit")
  else:
    result = 0
    a = a0
    while a > 0:
        r = a % 10
        result += r ** digit
        a //= 10
    #print("Result:", result)

    if(a0 == result):
      armstrongNumber += 1
      print(f"Armstrong Number {armstrongNumber}: {a0} ")
    if (armstrongNumber == n): break

    ad0 = 0
    a0square = 0
    result = 0
    result1 = 0