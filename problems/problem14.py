def next(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1

def collatz_len(n):
    i = 1
    while n != 1:
        n = next(n)
        i += 1
    return i

longest = 0

for n in range(1, 1000000):
    if(collatz_len(n) > longest):
        longest = collatz_len(n)
        print("%d contains %d terms" % (n, longest))
