from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests
import os

# A thread pool is a programming pattern for automatically managing a pool of worker threads
# It controls when the threads are created, such as just-in-time when they are needed
# It also controls what threads should do when they are not being used, such as making them wait
# without consuming computational resources.

base_url = "https://cataas.com//cat"
fetchCount = 20
singleThreadItems = []
multiThreadItems = []

def fetchCat(session):
    with session.get(base_url, stream=True) as r:
        return r.content

def main():

    # Measure time for single-threaded execution
    start_time0 = time.perf_counter()
    with requests.Session() as session:
        for x in range(fetchCount):
            singleThreadItems.append(fetchCat(session))

    end_time0 = time.perf_counter() - start_time0

    # Measure time for multi-threaded execution
    start_time1 = time.perf_counter()
    with requests.Session() as session:
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(fetchCat, session) for x in range(fetchCount)]
            for future in as_completed(futures):
                multiThreadItems.append(future.result())

    end_time1 = time.perf_counter() - start_time1

    print(f"Single thread: {len(singleThreadItems)} items fetched in {end_time0:.4f} seconds")
    print(f"Multithreading: {len(multiThreadItems)} items fetched in {end_time1:.4f} seconds")


if __name__ == "__main__":
    main()
