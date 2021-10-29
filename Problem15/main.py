def factorial(number, accumulator):
    if number == 1:
        return accumulator
    return factorial(number - 1, accumulator * number)


if __name__ == '__main__':
    start = time.time()
    n = 40
    k = 20

    n_factorial = factorial(n, 1)
    k_factorial = factorial(k, 1)
    n_k_factorial = factorial(n - k, 1)
    n_choose_k = n_factorial / (k_factorial * n_k_factorial)
    end = time.time()
    print(n_choose_k)
