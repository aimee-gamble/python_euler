import ajg_math

n = 2000000
s = 0

for x in range(0, n):
    if(ajg_math.is_prime(x)):
        s += x
    if x % 100 == 0:
        print("Currently at %d with a total of %d" % (x, s))

print("Total: %d" % (s))
