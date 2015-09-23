n = 2520
solved = False

while solved == False:
    n += 20
    solved = True
    for x in range(11,21):
        if(n % x != 0):
            solved = False
            break
    if solved == True:
        print(n)
