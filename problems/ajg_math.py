import math

def divisors(n):
    divisors = []
    sqrtn = math.ceil(math.sqrt(n))
    for i in range(1, sqrtn + 1):
        if n % i == 0 and n != i:
            divisors.append(i)
            if i != sqrtn and n / i != n and n / i != sqrtn:
                divisors.append(int(n / i))
    divisors.sort()
    return divisors

def reciprocal(n, dp):
    if isinstance(n, int) and isinstance(dp, int):
        result = "0."
        working = 1
        i = 0
        while working != 0 and i < dp:
            if working > n:
                result += str(working // n)
                working = working % n
                i += 1
            else:
                working = working * 10
        return result
    return None

def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    if n < 0:
        return False
    for i in range(2, math.ceil(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True
