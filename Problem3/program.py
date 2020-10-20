import time

start_time = time.time()
primes = [2]
factors = []
n = 600851475143


def next_prime():
    last = primes[-1]
    prime = False
    while not prime:
        last += 1
        prime = is_prime(last)
    return last


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


while n not in primes:
    # Loop through primes
    for prime in primes:
        # If prime is a factor
        if n % prime == 0:
            factors.append(prime)
            n //=  prime
            
    primes.append(next_prime())

factors.append(n)
print(factors)
print(max(factors))
print("Time: {} seconds".format(time.time() - start_time))
