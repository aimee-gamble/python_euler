import math

def get_c(a, b):
    x = (a ** 2) + (b ** 2)
    if(is_square(x)):
        return math.sqrt(x)
    return 0

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

for a in range (1, 999):
    for b in range(a, 999):
        c = get_c(a, b)
        if c > 0 and a+b+c == 1000:
            print("a = %d, b = %d, c = %d. Sum = %d" % (a, b, c, a+b+c))
            print("Product: %d" % (a*b*c))
