import math

def num_divisors(n):
    if n < 500 or n % 2 != 0:
        return 0

    divisors = 0
    if(n > 1):
        # number must be divisible by itself, except 1
        # 1 is included in the loop below
        divisors += 1

    sqrtn = math.ceil(math.sqrt(n))
    for i in range(1, sqrtn):
        if n % i == 0:
            divisors += 1
            if i != sqrtn:
                divisors += 1
    return divisors

i = 1
n = 0
divisors = 0

while divisors <= 500:
    n += i
    i += 1
    divisors = num_divisors(n)
    if(divisors > 200):
        print("%d: %d [16: %d, 32: %d]" % (n, divisors, n % 16, n % 32))
