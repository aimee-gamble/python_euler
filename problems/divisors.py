import math

def get_all(n):
    divisors = []
    sqrtn = math.ceil(math.sqrt(n))
    for i in range(1, sqrtn + 1):
        if n % i == 0 and n != i:
            divisors.append(i)
            if i != sqrtn and n / i != n and n / i != sqrtn:
                divisors.append(int(n / i))
    divisors.sort()
    return divisors
