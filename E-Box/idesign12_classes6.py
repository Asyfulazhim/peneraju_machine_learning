import datetime as dt

class Hall:
    def __init__(self, start_date, end_date, cost_per_day):
        self.start_date = start_date
        self.end_date = end_date
        self.cost_per_day = cost_per_day
        
    def noDays(self):
        return (self.end_date - self.start_date).days

    def cost(self):
        return self.noDays() * self.cost_per_day


# from Hall import Hall

d1 = input("Enter Start time (e.g., Dec 25 2017)\n")
d2 = input("Enter the End time (e.g., Dec 27 2017)\n")
cost = int(input("Enter the cost per day\n"))
#Fill your code here
start_date = dt.datetime.strptime(d1, "%b %d %Y")
end_date = dt.datetime.strptime(d2, "%b %d %Y")
hall = Hall(start_date, end_date, cost)
print("Total number of days", hall.noDays())
print("Total cost", hall.cost())