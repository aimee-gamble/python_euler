string = str(2 ** 1000)
total = 0

for i in range(0, len(string)):
    total += int(string[i])

print(total)
