import divisors

limit = 28123
total = 0

abundant = []
sumoftwo = [0] * (limit)

for n in range(1, limit):
    if(sum(divisors.get_all(n))) > n:
        abundant.append(n)

print("Found %d abundant numbers" % (len(abundant)))

len_abun = len(abundant)

for i in range(0, len_abun):
    for j in  range(i, len_abun):
        if(abundant[i] + abundant[j] < limit):
            sumoftwo[abundant[i] + abundant[j]] = 1

print("Found %d sums of two abundant numbers" % (len(sumoftwo)))

for n in range(1, limit):
    if sumoftwo[n] == 0:
        total += n

print("Found %d as the result" % (total))
