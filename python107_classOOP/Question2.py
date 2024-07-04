'''
Problem 2:
An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, 
however spaces and hyphens are allowed to appear multiple times.
Examples of isograms:
lumberjacks background downstream six-year-old
The word isograms, however, is not an isogram, because the s repeats.
Your task is to figure out if the user input is isogram
'''
class isogramChecker:
    def __init__(self):
        self.words = input().lower()
        self.words = self.words.replace(" ","")
        self.words = self.words.replace("-","")
        print(self.words)
    def check(self):

        return len(self.words) == len(set(self.words))
        
checker = isogramChecker()
if checker.check():
    print("The word is a Isogram!")
else:
    print("The word is not a Isogram.")


# #words = input()
# words = "LuMbeR-Ja ck"
# words = words.lower()
# words = words.replace(" ","")
# words = words.replace("-","")
# print(words)

# if len(words) == len(set(words)):
#     print("Isogram")
# else:
#     print("Not an isogram")



#for 
