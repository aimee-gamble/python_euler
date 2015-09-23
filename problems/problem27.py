import ajg_math

def f(n, a, b):
    return (n ** 2) + (a * n) + b

def num_remarkable(a, b):
    n = 0
    while True:
        if not ajg_math.is_prime(f(n, a, b)):
            return n - 1
        n += 1

result = [0, 0, 0]

for a in range(-999, 1000):
    for b in range(-999, 1000):
        num = num_remarkable(a, b)
        if num > result[0]:
            result = [num, a, b]

print(result)
print(result[1] * result[2])
