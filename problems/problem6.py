sum_of_squares = 0
sum_of_numbers = 0

for x in range(1,101):
    sum_of_numbers += x
    sum_of_squares += x * x

square_of_sums = sum_of_numbers ** 2

print(square_of_sums - sum_of_squares)
