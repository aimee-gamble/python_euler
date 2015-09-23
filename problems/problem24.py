import itertools
x = itertools.permutations(range(10), 10)
counter = 0

for i in x:
    counter += 1
    if counter == 1000000:
        print(i)
    else:
        pass
