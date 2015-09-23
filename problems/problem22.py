value = { 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, }

def score(index):
    s = 0
    name = data[index]
    for i in range(len(name)):
        s += value[name[i]]
    return (index + 1) * s

with open ("problem22.txt", "r") as datafile:
    data = datafile.read().split(",")

for i in range(len(data)):
    data[i] = data[i][1:-1]

data.sort()

total = 0

for i in range(len(data)):
    total += score(i)

print(total)
