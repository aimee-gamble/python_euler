import ajg_math

def longest_repeat(n, min_len):
    dp = len(n)
    longest = 0

    for i in range(0, dp // 2):
        for j in range(1, dp // 2):
            if (dp // (j + 2)) > 1 and (n.count(n[i:(i+j)] * (dp // (j + 2)))) >= 1:
                return j
    return 0

dp = 5000
longest = 1
result = 1


for n in range(1,1000):

    reciprocal = ajg_math.reciprocal(n, dp)
    dp_range = reciprocal[2:len(reciprocal)]

    repeat_len = 0

    if len(dp_range) == dp:
        repeat_len = longest_repeat(dp_range, longest)

        if repeat_len > longest:
            result = n
            longest = repeat_len

print(result, longest)
