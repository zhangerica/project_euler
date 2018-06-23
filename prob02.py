#fibonacci sequence 1, 2, 3, ...
#consider the terms in the fibonacci sequence whose values do not exceed 4 million, find the sum of the even-valued terms

m, n = 1, 2
sum = n
max = 4*10**6
while m <= max:
    m += n
    n += m
    if m % 2 == 0:
        sum += m
    if n % 2 == 0:
        sum += n

print sum
