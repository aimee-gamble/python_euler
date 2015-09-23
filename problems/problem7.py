import math

def is_prime(n):
    for x in range(2, math.ceil(math.sqrt(n) + 1)):
        if(n % x == 0):
            return False
    return True

x = 3
y = 2

while y < 10001:
    x += 2
    if(is_prime(x)):
        y += 1
        print("Found prime # %d: %d" % (y, x))
