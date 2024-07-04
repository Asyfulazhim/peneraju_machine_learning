
# Prob 1
def count_char(filename):
    with open(filename,'r') as file:
        text = file.readlines()
        new = ' '.join(text).strip().replace(' ','')
        words = sorted(new.lower())

        char_Dict = {}
        for char in words:
            if char not  in char_Dict:
                char_Dict[char] = 1
            else:
                char_Dict[char] += 1
        
        for key, value in char_Dict.items():
            print(f"{key}: {value}")
    #print(char_Dict)

count_char('frequencyFile.txt')

# Prob 2
n = int(input())
data = []
for _ in range(n):
    name = input()
    salary = input()
    data.append((name, salary))

data.sort()

with open("salaryData.csv", "w") as f:
    for name, salary in data:
        f.write(f"{name},{salary}\n")