# Problem 10
# Write a simple python function that accepts a hyphen-separated sequence of words as parameter 
# and returns the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def string_sorting(string):
  words = string.split('-')
  words.sort()
  words = '-'.join(words)
  return words

string_input = input("Enter hyphen-separated sequence of word:")
print("after sorting them alphabetically", string_sorting(string_input))