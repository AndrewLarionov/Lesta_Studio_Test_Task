from typing import List


def timsort(array: List) -> List:
    """Алгоритм сортировки Timsort"""
    min_run: int = 32
    n: int = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size: int = min_run
    while size < n:

        for start in range(0, n, size * 2):

            midpoint: int = start + size - 1
            end: int = min((start + size * 2 - 1), (n-1))

            merged_array: List = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            array[start:start + len(merged_array)] = merged_array

        size *= 2

    return array


def merge(left, right) -> List:
    """
    Объединяет массивы создавая отсортированный массив
    """
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result: List = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def insertion_sort(array, left=0, right=None) -> List:
    """Алгоритм сортировки вставкой модифицированный для использования в Timsort"""
    if right is None:
        right: int = len(array) - 1

    for i in range(left + 1, right + 1):

        key_item = array[i]

        j = i - 1

        while j >= left and array[j] > key_item:

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item
    return array
