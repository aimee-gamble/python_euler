first = 1
second = 1
current = 2
length = 1
index = 3

while length < 1000:
    first = second
    second = current
    current = first + second

    length = int(len(str(current)))
    index += 1

print(index)
