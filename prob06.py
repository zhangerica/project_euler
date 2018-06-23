# sum of the squares of the first 10 natural numbers is 1^2 + 2^2 + ... + 10^2 = 385
# square of the sum of the first 10 natural numbers if (1 + 2 + ... + 10)^2 == 55^2 = 3025
# difference b/t sum of the squares of thef first 10 natural numbers & the square of the sum is 3025 - 385 = 2640
# find difference b/t sum of the squares of the first one hundred natural numbers & the square of the sum

i = 1
sum_squares = i**2
while i < 100:
    i += 1
    sum_squares += i**2

j = 1
sum = j
while j < 100:
    j += 1
    sum += j

print sum**2 - sum_squares
