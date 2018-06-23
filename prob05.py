#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 w/o any remainder
#smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 2520
m = [i for i in range(1, 21)]
zeros = [0 for i in range(1, 21)]
r = [n % j for j in m]

while r != zeros:
    n += 2520
    r = [n % j for j in m]
    print r

print n
