#the sums of the primes below 10 is 17. Find the sum of all the primes below 2 million
#not the best solution; took 30 min
primes = [2, 3, 5, 7, 11, 13]

def is_prime(number):
    for m in primes:
        if number % m == 0:
            return False
    return True

def list_primes_below(max):
    last = primes[-1]
    while last < max:
        next = last + 2
        if is_prime(next):
            primes.append(next)
        last = next
        print last
    return primes

"""
#max difference b/t 2 consecutive primes
def max_distance(list):
    i = 0
    distance = 0
    while i < len(list)-1:
        new_distance = list[i + 1] - list[i]
        if new_distance > distance:
            distance = new_distance
        i += 1
    return distance
"""

print sum(list_primes_below(2000000))
