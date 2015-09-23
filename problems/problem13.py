with open("problem13.txt") as f:
    grid = f.readlines()

total = 0

for i in range(0, len(grid)):
    total += int(grid[i])

print(total)
