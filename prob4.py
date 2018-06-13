#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3-digit numbers

def is_palindrome(number):
    if number < 0:
        print('number must be nonnegative')
    elif number // 10 == 0:
       return True
    else:
        return is_array_palindrome(separate_digits(number))

def separate_digits(number):
    digits = []
    while number > 9:
        last = number % 10
        digits.append(last)
        number = number // 10
    digits.append(number)
    return digits

def is_array_palindrome(digits):
    if digits == [] or len(digits) == 1:
        return True
    else:
        while digits[0] == digits[-1]:
            return is_array_palindrome(digits[1:-1])
    return False

arr = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i*j):
            print True
            arr.append(i*j)

print max(arr)
