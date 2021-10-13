import time

# memoization point:steps
cache = {1: 1}


def calculate_steps(staring_point):
    point = staring_point
    step = 1

    while point != 1:
        # calculated
        calculated = cache.get(point)
        if calculated is not None:
            step += calculated - 1
            return step

        # odd
        if point % 2 != 0:
            point = (point * 3 + 1) // 2
            step += 2
        # even
        else:
            point = point // 2
            step += 1

    return step


if __name__ == '__main__':
    # start time
    start = time.time()

    # program
    max_steps = 1
    max_steps_number = 1
    for i in range(1, 1000000):
        current_number = i
        steps = calculate_steps(i)
        cache[i] = steps
        if steps > max_steps:
            max_steps = steps
            max_steps_number = i

    end = time.time()
    print(f'Time: {end - start} s')
    print(f'Steps: {max_steps}')
    print(f'Number: {max_steps_number}')
