'''
string_input = input("Enter numbers separated by commas: ")
numbers = string_input.split(",")
#number = list(map(int,numbers))
numbers = [int(num) for num in numbers]
print(numbers)
unique = set()
combination1 = []
fullcombination = []
# to elliminate same number input by user
for num in numbers:
  for u in unique:
    if num == u:
      continue
  unique.add(num)
print(unique)

found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 100:
                print("Triplet found:", numbers[i], numbers[j], numbers[k])
                combination1.append(numbers[i])
                combination1.append(numbers[j])
                combination1.append(numbers[k])
                fullcombination.append(combination1)

                found = True
                continue
            #else: combination1.clear
        if found: continue
    #combination1.clear()
    if found:continue
if not found:
    print("No triplet found")

print(combination1)
print(fullcombination)
# add code to remove the same number in the list
'''
n = int(input())
data = {}

for i in range(n):
    line = input()
    name, *scores = line.split()
    data[name] = list(map(int, scores))

choose = input()
print(data)


#found = True
for f in data:
    if f == choose:
        choosen_marks = data[choose]
        choosen_marks.sort()
        print(choosen_marks[2])
        for a in range(len(choosen_marks)-1):
            if [a] == choosen_marks[a+1]:
                print(f"{choose} scored same marks in all subjects: {choosen_marks[a]}")
        break
        
else:
    print("Student doesn't exist")
'''
choosen_marks = data[choose]
choosen_marks.sort()
print(choosen_marks[2])
'''
for a in range(len(choosen_marks)-1):
    if [a] == choosen_marks[a+1]:
        print(f"{choose} scored same marks in all subjects: {choosen_marks[a]}")
