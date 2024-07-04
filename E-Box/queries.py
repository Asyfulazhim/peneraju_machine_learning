# any / all
# any: True if any element of the iterable is true. If the iterable is empty, return
# False.

givennumber = 11
divisors = range(2, givennumber)

if any([givennumber % mynumber == 0 for mynumber in divisors]):
    print("The number is not a prime number")
else:
    print("The number is a prime number")
