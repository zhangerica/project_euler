# prime factors of 13195 are 5, 7, 13 and 29
# what is the largest prime factor of 600851475143

n = 600851475143
arr = []

def largest_prime_fact(number):
    if number == 0 or number == 1:
        print('number must be greater or equal to 2')
    if number % 2 == 0:
        if number == 2:
            print(2)
        else:
            arr.append(2)
            div = number/2
            largest_prime_fact(div)
    else:
        largest_odd_prime_fact(number)

def largest_odd_prime_fact(number):
    if number == 1:
        print arr[-1]
    else:
        i = 3
        fact = 0
        key = True
        m = 0
        while key: 
            if number % i == 0:
                fact = i
                m = number/fact
                arr.append(fact)
                key = False
                largest_odd_prime_fact(m)
            else:
                i += 2

largest_prime_fact(n)




        
