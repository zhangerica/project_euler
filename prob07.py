# first six prime numbers 2, 3, 5, 7, 11, 13
# 6th prime is 13
# find the 10001st prime number

primes = [2, 3, 5, 7, 11, 13]

def is_prime(number):
    if number < 2:
        return "number must be greater than 1"
    else:
        for m in primes:
            if number == m:
                return True
            elif number % m == 0:
                return False
        return True

def nth_prime(i, prime, n):
    while i < n:
        next = prime + 2
        if is_prime(next):
            primes.append(next)
            i += 1
            prime = next
        else:
            return nth_prime(i, next, n)
    return prime
"""
step = 100
j = 6
prime_number = 13

while j < 9900:
    next = j + step
    prime_number = nth_prime(j, prime_number, next)
    j = next

print nth_prime(j, prime_number, 10001)
"""
