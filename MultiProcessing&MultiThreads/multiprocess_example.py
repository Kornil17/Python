from time import perf_counter
from multiprocessing import Process, current_process
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        print(f"Func was done with time -> {perf_counter() - start}")
    return wrapper


@timer
def func_counter(count_to: int) -> None:
    count = 0
    print(f"process -> {current_process()} has been started")
    while count < count_to:
        count += 1
    print(f"process -> {current_process()} has been done")


def main():
    process_1 = Process(target=func_counter, args=(1_000_000,), name="Process_1")
    process_2 = Process(target=func_counter, args=(2_000_000,), name="Process_2")

    process_1.start()
    process_2.start()

    process_2.join()
    process_1.join()


if __name__ == "__main__":
    main()
