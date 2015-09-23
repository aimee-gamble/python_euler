digits = 4
total = 0

with open("problem11.txt") as f:
    grid = f.readlines()

for i in range(0, len(grid)):
    grid[i] = grid[i].split(" ")

for y in range(0, len(grid) - digits + 1):
    for x in range(0, len(grid[y]) - digits + 1):
        num = [1, 1, 1, 1]
        diagonal = ""
        for i in range(0, digits):
            num[0] *= int(grid[y + i][x])
            num[1] *= int(grid[y][x + i])
            num[2] *= int(grid[y + i][x + i])
            num[3] *= int(grid[y + i][x + digits - 1 - i])
            diagonal += " " + grid[y + i][x + i]
        maximum = max(num)
        if(maximum > total):
            total = maximum

print(total)
