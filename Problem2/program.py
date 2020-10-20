fib_numbers = [1, 2]
total = 0

four_million = 4 * 10 ** 6

while fib_numbers[-1] < four_million:
    fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

del fib_numbers[-1]

for i in fib_numbers:
    if i & 1 == 0:
        total += i


print(total)
