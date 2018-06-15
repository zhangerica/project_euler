#pythagorean triplet is a set of 3 natural numbers a < b < c for which a^2 + b^2 = c^2
#for example, 3^2 + 4^2 = 5^2
#there exists exactly 1 pythagorean triplet for which a + b + c = 1000
#find the product a*b*c

from math import sqrt

squares = [n**2 for n in range(1, 500)]

for a in squares:
    for b in squares:
        for c in squares:
            if a + b == c:
                if sqrt(a) + sqrt(b) + sqrt(c) == 1000:
                    print sqrt(a)*sqrt(b)*sqrt(c)
