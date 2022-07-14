import timeit


def isEven(value: int) -> bool:
    """
    Определяет четность целого числа через взятие модуля
    """
    return value % 2 == 0


def isEven_2(value: int) -> bool:
    """
    Определяет четность целого числа через логическое "И"
    """
    return value & 1 == 0


if __name__ == '__main__':

    print(isEven(124))
    print(isEven_2(124))
    print(isEven(125))
    print(isEven_2(125))

    print(timeit.timeit("isEven(125)", setup="from __main__ import isEven", number=10000000))
    print(timeit.timeit("isEven_2(125)", setup="from __main__ import isEven_2", number=10000000))


