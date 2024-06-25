# Problem 3
# Get number of items as input and generate that many ADAM Numbers

n = int(input ("enter any number:" ))
adamNumber = 0
for a0 in range(1, 1000):
  result = 0
  temp = a0
  while temp > 0:
    result = (result * 10) + (temp % 10)
    temp //= 10

  ad0 = result ** 2     #square the reserve input
  a0square = a0 ** 2    #square the input

  result1 = 0
  temp1 = ad0
  while temp1 > 0:
    result1 = (result1 * 10) + (temp1 % 10)
    temp1 //= 10

  if(a0square == result1):
    adamNumber += 1
    print(f"Adam number {adamNumber}: {a0} ")
  if (adamNumber == n): break