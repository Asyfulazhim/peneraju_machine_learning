# Problem 3 GCD Calculation: Euclidean algorithm.

def GCD(N1, N2):
    while N2 != 0:
        print(f"GCD({N1},{N2}) =", end=" ")
        N1, N2 = N2, N1 % N2
    print(f"GCD({N1},{N2}) = {N1}")
    return N1

A = int(input("A: "))
B = int(input("B: "))

if A > B:
    gcd = GCD(A, B)
else:
    gcd = GCD(B, A)