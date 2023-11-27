import time
from threading import Thread
from random import randint


def sum_all_list(numbers, results, id):
    results[id] = sum(numbers)


def get_list_deviation(numbers, threads_number):
    list_length = len(numbers)

    chunk_size = list_length // threads_number or 1

    chunk_start_index = 0
    chunk_end_index = chunk_start_index + chunk_size

    deviation = []

    for i in range(threads_number):
        chunk = numbers[chunk_start_index: chunk_end_index]
        deviation.append(chunk)

        chunk_start_index = chunk_end_index
        chunk_end_index += chunk_size

        if list_length - chunk_end_index < chunk_size:
            chunk_end_index = list_length

    return deviation


def estimate_sum(numbers: list[int], threads_count: int):
    """
    Функция вычисляет сумму всех чисел списка в многопоточном режиме.
    """
    sums = {}

    deviation = get_list_deviation(numbers, threads_count)

    for thread in range(threads_count):
        thread = Thread(target=sum_all_list, args=(deviation[thread], sums, thread))
        thread.start()

    sum = 0

    thread = 0
    while thread < threads_count:
        chunk_sum = sums.get(thread)

        if type(chunk_sum) is not None:
            sum += chunk_sum
            thread += 1

    return sum


def test_estimate_sum():
    some_list = [randint(-100, 100) for _ in range(100000)]
    threads = randint(1, 16)

    for i in range(100):
        assert estimate_sum(some_list, threads) == sum(some_list)


if __name__ == '__main__':
    test_estimate_sum()
