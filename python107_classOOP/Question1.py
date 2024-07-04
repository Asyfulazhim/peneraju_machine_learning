'''
A pangram is a sentence using every letter of the alphabet at least once. 
It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
Example: The quick brown fox jumps over the lazy dog.
Your task is to figure out if a sentence is a pangram.
'''
#use class to solve this problem
class PangramChecker:
    def __init__(self, sentence):
        self.sentence = sentence.lower()
        self.alphabet = set('abcdefghijklmnopqrstuvwxyz')
        print(self.sentence)

    def check(self):
        return set(self.sentence).issuperset(self.alphabet)
        
checker = PangramChecker("The quick brown fox jumps over the lazy dog")
if checker.check():
    print("The sentence is a pangram!")
else:
    print("The sentence is not a pangram.")