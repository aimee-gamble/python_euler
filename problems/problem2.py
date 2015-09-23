total = 2

x = 1
y = 2

while y < 4000000:
    z = x + y
    x = y
    y = z
    if y % 2 == 0:
        total += y

print(total)
