import multiprocessing
import math
import multiprocessing.pool
import time

number_count = 15000
numbers = []
for i in range(number_count):
    numbers.append(i)

single_core_factorials = []
multi_core_factorials = []

def calculate_factorial(n):
    return math.factorial(n)


def main():
    startTime = time.perf_counter()

    startTime_single = time.perf_counter()
    # single core
    for number in numbers:
        single_core_factorials.append(calculate_factorial(number))
    endTime_single = time.perf_counter() - startTime_single

    startTime_multi = time.perf_counter()

    # creating a pool
    with multiprocessing.Pool() as pool:
        multi_core_factorials = pool.map(calculate_factorial, numbers)

    endTime_multi = time.perf_counter() - startTime_multi
    endTime = (time.perf_counter() - startTime)

    print(f"Single-core: {len(single_core_factorials)} factorials calculated in {endTime_single:.4f} seconds")
    print(f"Multicore: {len(multi_core_factorials)} factorials calculated in {endTime_multi:.4f} seconds")
    print(f"Total time: {endTime:.4f}")

if __name__ == "__main__":
    main()
