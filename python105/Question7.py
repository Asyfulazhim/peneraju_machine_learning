# Problem 7 Harmonic Series:
n = int(input())
sum = 0
for i in range(1,n+1):
  sum += (1/i)

print (f"sum = {sum:.2f}")