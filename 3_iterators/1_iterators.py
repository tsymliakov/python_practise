class List2_editable_start:
    """
    Задание 1. Класс- итератор с конструктором, через который задается начальное
    значение.
    """
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count < 10:
            return current
        raise StopIteration


class List2_with_flag:
    """
    Задание 2. Класс- итератор, который получает длину генерируемой
    последовательности и флаг через конструктор, по которому либо останавливает
    выдачу значений при достижении длины границы, либо начинает повторно
    генерировать такую же последовательность.
    """
    def __init__(self, bound, is_infinite = False):
        if bound < 0:
            raise ValueError("bound must be positive")
        if type(bound) is not int:
            raise ValueError("bound must be integer")

        self.bound = bound
        self.is_infinite = is_infinite

    def __iter__(self):
        self.start = 1
        self.count = 0
        return self

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1

        if self.count <= self.bound:
            return current

        if self.is_infinite:
            self = self.__iter__()
            return self.__next__()

        raise StopIteration
