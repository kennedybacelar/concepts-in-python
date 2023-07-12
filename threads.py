from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time
import os
import flock

FILENAME = "sample.txt"


def task1():
    signature = f"Task-I-1"
    with open(FILENAME, "a+") as f:
        with flock.Flock(f.fileno(), flock.LOCK_EX):
            for i in range(10):
                f.write(f"{signature} {datetime.now()}\n")
                time.sleep(3)


def task2():
    signature = f"Task-II-2"
    with open(FILENAME, "a+") as f:
        with flock.Flock(f.fileno(), flock.LOCK_EX):
            for i in range(10):
                f.write(f"{signature} {datetime.now()}\n")
                time.sleep(3)


def main():
    start_time = time.time()
    foo_str = "ken-foo"
    pool = ThreadPoolExecutor()
    pool.submit(task1)
    pool.submit(task2)
    with open(FILENAME, "a+") as f:
        with flock.Flock(f.fileno(), flock.LOCK_EX):
            f.write(f"{foo_str}\n")
    end_time = time.time()

    final_execution_time = round((end_time - start_time), 3)
    print(f"Execution time: {final_execution_time}")


if __name__ == "__main__":
    main()
