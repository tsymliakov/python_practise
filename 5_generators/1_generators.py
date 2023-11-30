def long_process(id, n):
    sum = 0

    for x in range(n):
        sum += x+1
        print(id, sum)
        yield sum
    yield sum


def get_many_generators(*length : int):
    """
    Принимает набор чисел, возвращает список генераторов long_process
    """
    return [long_process(str(i), l) for i, l in enumerate(length)]
