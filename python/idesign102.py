# Question 2
NP1 = int(input("Enter the number of people who watched show 1\n"))
AR1 = float(input("Enter the average rating for show 1\n"))
NP2 = int(input("Enter the number of people who watched show 2\n"))
AR2 = float(input("Enter the average rating for show 2\n"))
NP3 = int(input("Enter the number of people who watched show 3\n"))
AR3 = float(input("Enter the average rating for show 3\n"))

TotalAverage = ((NP1 * AR1) + (NP2 * AR2) + (NP3 * AR3)) / (NP1 + NP2 + NP3)

print(f"The overall average rating for the show is {TotalAverage:.2f}")