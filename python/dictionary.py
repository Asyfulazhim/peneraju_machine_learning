
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friend_ages["Rolf"])

friend_ages["Rolf"] = 20    #update rolf ages
friend_ages["Bob"] = 25     #add bob detail to list

print(friend_ages)

friend = (
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
)

print(friend[0]["name"])

# List of Tuple
friends = [("Rolf",24),("Adam",30),("Anne", 27)]
# turn the list to dictionary
friends_ages = dict(friends)
print(friends_ages)

a={1,2,3}
b={1,2,3,4}
c=a.issuperset(b)
print (c)

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

science_but_not_art = science_friends.difference(art_friends)
print(science_but_not_art)

# not in both
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

# intersec
in_both = art_friends.intersection(science_friends)
print(in_both)

# union
all_friends = art_friends.union(science_friends)
print(all_friends)

