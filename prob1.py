#natural numbers below 10 that are multiples of 3 or 5: 3, 4, 6, 9
#sum of these multiples is 23
#find sum of all multiples of 3 or 5 below 1000

sum = 0

for n in range(1, 1000):
   if n % 3 == 0 or n % 5 == 0:
      sum += n
   n += 1

print sum
