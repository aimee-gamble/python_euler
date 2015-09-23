import math

n = 600851475143
s = False
d = 2

while s == False:
    if(n % d == 0):
        # we have found a factor
        x = n / d
        #is x a prime?
        if(x % 2 != 0):
            s = True
            for y in range(2, math.ceil(math.sqrt(x))):
                if(x % y == 0):
                    # we have found another factor
                    s = False
                    break
        print("Factor: %d, Prime: %s" % (x, s))
    d += 1
