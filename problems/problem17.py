words = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

def wordit(n):
    if n < 100:
        if n in words:
            return words[n]
        return words[(n // 10) * 10] + words[n % 10]
    if n < 1000:
        if n % 100 == 0:
            return words[(n // 100)] + words[100]
        return words[(n // 100)] + words[100] + 'and' + wordit(n % 100)
    return words[(n // 1000)] + words[1000]

t = 0

for n in range(1, 1001):
    t +=len(wordit(n))

print(t)
