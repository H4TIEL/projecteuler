import math
import time


def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    # checks exceptions 2 and 3
    if n <= 3:
        return n > 1
    # checks 6k+0, 6k + 2, 6k + 3 and 6k + 4
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gen_primes(n: int) -> list[int]:
    primes = [2, 3, 5]
    i = 1
    # increment by check 6k+1 or 6k+5
    while primes[-1] < n:
        x = 6 * i + 1
        y = 6 * i + 5
        if is_prime(x):
            primes.append(x)
        if is_prime(y):
            primes.append(y)
        i += 1

    return primes


def upper_bound_nth_prime(n: int) -> float:
    if n < 6:
        return 13

    return n * (math.log(n) + math.log(math.log(n)))


def is_prime_number(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    start_time = time.time_ns()
    limit = 2000000
    primes_list = gen_primes(limit)
    primes_list.pop()
    print(sum(primes_list))
    end_time = time.time_ns()
    print(end_time - start_time, 'ns')
