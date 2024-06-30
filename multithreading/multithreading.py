import threading
import time
import requests

# Multithreading is useful for tasks that are I/O bound.

# Multithreading is a technique that allows a program to run multiple
# tasks concurrently within a single process.
# Each task is executed in its own thread, which is a lightweight unit of execution
# that shares the same memory space as other threads in the process

base_url = "https://cataas.com//cat"

def fetchCat(i):
    for x in range(i):
        response = requests.get(base_url,stream=True)


def main():
    start_time0 = time.perf_counter()
    fetchCat(10)
    end_time0 = time.perf_counter() - start_time0

    start_time1 = time.perf_counter()
    # To create a new thread, we create an object of the Thread class. It takes the ‘target’ and ‘args’ as the parameters.
    t1 = threading.Thread(target=fetchCat, args=(5,))
    t2 = threading.Thread(target=fetchCat, args=(5,))

    # To start a thread, we use the start() method of the Thread class
    t1.start()
    t2.start()

    # In order to stop the execution of the current program until a thread is complete, we use the join() method
    # As a result, the current program will first wait for the completion of t1 and then t2.
    # Once, they are finished, the remaining statements of the current program are executed
    t1.join()
    t2.join()
    end_time1 = time.perf_counter() - start_time1

    print("Single thread done in ", end_time0, " seconds")
    print("Multithreading done in ", end_time1, " seconds")


if __name__ == "__main__":
    main()
