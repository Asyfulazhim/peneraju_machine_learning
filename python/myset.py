# set uses {}
# set is modifiable (add, edit and delete)
# set is unordered
# set does not allow duplicate values
# set is not indexed

# this is first time we are using {}
x = {10,20,30,40,50,70,10,40}
print(x)

# what do you observe
# 1. unordered
# 2. no duplicates
# 3. no indexing
# 4. modifiable
# 5. no slicing
# 6. no repetition
# 7. no concatenation

# since set is not indexed you cannot retrieve the value using [] syntax
# only way is using
# 1. for loop
# 2. in operator
# 3. set methods
# 4. list conversion
# 5. tuple conversion

for i in x:
    print(i)

# modifiable
fruits = {"apple", "orange", "mango"}
fruits.add("banana")
print(fruits)

# to delete an item in set
fruits.remove("orange")
print(fruits)

# pop => randomly remove item
fruits.pop()
print(fruits)

fruits = ["apple", "mango","Orange", "mango", "apple","banana", "grapes", "apple"]
uniquefruits = set(fruits)
print(uniquefruits)

overseafruits = {"apple","orange","mango","grapes","banana"}
localfruits = {"durian","rambutan", "cempedak","banana","mangosteen"}
print(overseafruits.union(localfruits))
print(overseafruits.intersection(localfruits))
print(overseafruits.difference(localfruits))
print(localfruits.difference(overseafruits))

favouritefruits = {"durian", "rambutan", "mangosteen"}
print(favouritefruits.issubset(localfruits)) # True
print(favouritefruits.issubset(overseafruits)) # False
print(localfruits.issuperset(favouritefruits)) # True
print(favouritefruits.isdisjoint(overseafruits)) # False

content = """It does not have to be a button — in this case it is a barely noticeable link. 
But spammers use such links to verify that your email account is active. This information 
will go further — and you will get spam bombed. Even worse, such links may lead to compromised 
websites that can be used for phishing or installing dangerous software on your device.
Clicking on unsubscribe links in spam emails or responding to them is dangerous. That is why 
if you come across a suspicious email, just delete it from your inbox. You can also flag such 
emails as spam if the filter did not catch them — this will protect you from receiving more 
emails from the same address."""

words = content.split()
print(len(words))
unique_words = set(words)
print(len(unique_words))
print(unique_words)

cleanwords = []
for word in words:
    word = word.replace(".,!?:;","")
    word = word.lower()
    cleanwords.append(word)

unique_words = set(cleanwords)
print(len(unique_words))
print(unique_words)

#common_words
common_words = {"the", "and", "a", "is", "in", "that"}
unique_words = unique_words.difference(common_words)

print(len(unique_words))

# we have another library called NLTK
# require for NLP 

spamwords = {"suspicious","dangerous","trick","phishing", "spammer"}
spamword = unique_words.intersection(spamwords)

print(len(spamword))

