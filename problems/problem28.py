def layer(i):
    return 16 * (i ** 2) + (4 * i) + 4

result = 1

for n in range(1, 501):
    result += 16 * (n ** 2) + (4 * n) + 4

print("Layer %d (%dx%d) diagonals total %d" % (n, (2*n+1), (2*n+1), result))
