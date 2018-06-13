#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3-digit numbers

def is_palindrome(number):
    if number < 0:
        print('number must be nonnegative')
    elif number < 10:
       return True
    else:
        return is_list_palindrome(list_of_digits(number))

def list_of_digits(number):
    digits = []
    while number > 9:
        last = number % 10
        digits.append(last)
        number = number // 10
    digits.append(number)
    return digits

def is_list_palindrome(list):
    if list == [] or len(list) == 1:
        return True
    else:
        while list[0] == list[-1]:
            return is_list_palindrome(list[1:-1])
    return False

list = []

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i*j):
            list.append(i*j)

print max(list)
