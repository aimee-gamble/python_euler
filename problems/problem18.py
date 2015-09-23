with open("problem18.txt") as f:
    triangle = f.readlines()

for i in range(0, len(triangle)):
    triangle[i] = triangle[i].split(" ")

def next(x, y):
    if y + 1 >= len(triangle):
        return int(triangle[y][x])
    lpath = int(triangle[y][x]) + next(x, y + 1)
    rpath = int(triangle[y][x]) + next(x + 1, y + 1)
    if lpath > rpath:
        return lpath
    return rpath

print(next(0,0))
