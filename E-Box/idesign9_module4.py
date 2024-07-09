'''
Input Format:
The first line of input is a string consists of lower case letter words  (each word will indicate topics selected by the student)


Output Format:
The output consists of a count of each word.

Note: All text in bold corresponds to the input and the rest corresponds to output.

Sample Input and Output:
mother father mother GST father GST facebook facebook GST
facebook-2
father-2
gst-3
mother-2

'''
words = input("Enter the String\n").lower().split(" ")
words.sort()

dict = {}
for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

#dict = {'facebook': 2, 'father': 2, 'gst': 3, 'mother': 2}

for key, value in dict.items():
    print(f"{key}-{value}")


