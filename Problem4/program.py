import time


start = time.time()


def is_palindrome(number):
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    reverse = 0
    while number > reverse:
        reverse = reverse * 10 + (number % 10)
        number //= 10
    return number == reverse or number == reverse // 10


def largest_palindrome_product():
    palindrome = 0
    for a in range(999, 500, -1):
        for b in range(999, 500, -1):
            product = a * b
            if is_palindrome(product) and product > palindrome:
                print("a: {} b: {} product: {}".format(a, b, product))
                palindrome = product
    return palindrome


print(largest_palindrome_product())

print("Time: {}s".format(time.time() - start))

