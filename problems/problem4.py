import math

def is_palindrome(number):
    string = str(number)
    for i in range(0,math.ceil(len(string) / 2)):
        if(string[i] != string[len(string) - 1 - i]):
            # we are not a palindrome
            return False
    return True

print(is_palindrome(675))

largest = 0

for x in range(1000,99,-1):
    for y in range(1000,99,-1):
        z = x * y
        if(is_palindrome(z) and z > largest):
            largest = z
            print("%d x %y = %z", (x, y, z))
