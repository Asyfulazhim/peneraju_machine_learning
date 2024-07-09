n = int(input())
#n = 10
#initialize first two Fibonacci numbers
a = 0
b = 1
print(a,b, end=" ")
for num in range (1,n-1):
  a,b = b, a + b
  print(b,end=" ")   