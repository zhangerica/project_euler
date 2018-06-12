#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3-digit numbers

def is_palindrome(number):
    if number < 0:
        print('number must be nonnegative')
    elif number // 10 == 0:
       return True
    else:
        last = number % 10
        first = first_digit(number)[0]
        num_dig = first_digit(number)[1]
        if first == last:
            truncated = truncate(number, first, num_dig)
            print truncated
            return is_palindrome(truncated)
        else:
            return False
            
def truncate(number, first, num_dig):
    return (number - first * 10 ** (num_dig - 1) - number % 10) / 10

def first_digit(number):
    if number == 0:
        print('must be a natural number')
    else:
        i, digits = 1, number
        while digits // 10:
            digits = digits // 10
            i += 1
        first = digits % 10
        num_dig = i
        return first, num_dig
"""
arr = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i*j):
            print True
            arr.append(i*j)

print arr
"""
print truncate(7017, 7, 4)