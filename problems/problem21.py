import math

def d(n):
    result = 0
    sqrtn = math.ceil(math.sqrt(n))
    for i in range(1, sqrtn + 1):
        if n % i == 0:
            result += i
            if i != sqrtn and n / i != n:
                result += int(n / i)
    return result

store = [0]
amicable = []

for n in range(1, 10000):
    store.append(d(n))

print(store)

for (i, value) in enumerate(store):
    if value < len(store) and i != value and store[value] == i:
            amicable.append(i)

print(len(amicable))
print(sum(amicable))
