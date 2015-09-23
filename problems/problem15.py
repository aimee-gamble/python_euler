size = 20
options = [[0] * (size + 1)] * (size + 1)
total = 0

for x in range(size, -1, -1):
    for y in range(size, -1, -1):
        if x == size and y < size:
            options[x][y] = 1
        elif y == size and x < size:
            options[x][y] = 1
        elif x < size and y < size:
            options[x][y] = options[x + 1][y] + options[x][y + 1]
        print("Options for [%d,%d]: %d" % (x, y, options[x][y]))
