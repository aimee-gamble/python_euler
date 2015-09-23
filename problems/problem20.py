f = 1
t = 0

for n in range(1, 101):
    f *= n

s = str(f)

for i in range(0, len(s)):
    t += int(s[i])

print(t)
