import numpy as np
import mypy as mp
import random as rnd
from time import process_time


class SortingNameError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        result = 'Invalid name of sorting (should be "comb", )'
        if self.message:
            result += f'. {self.message}'

        return result


class ListParameterError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        result = 'The parameter of sorting function should be list'
        if self.message:
            result += f'. {self.message}'

        return result


class Sorting:
    def __init__(self) -> None:
        self.sorting = {
            'comb': comb_sort,
            'gnome': gnome_sort,
            'heap': heap_sort
        }
        self.name = None

    def set_algorithm(self, name: str) -> None:
        self.name = name

    def test_sorting(self) -> None:
        if not self.name:
            print('\033[31mYou should choose the algorithm!\033[0m\n')
            return

        i = 0
        failed_tests = ''
        print('------------------')
        print(f'\033[1m\033[34mNAME: {self.name}\033[0m')
        print('------------------')
        print('--START TESTING---')
        print('------------------')
        for n in range(1, 102, 10):
            i += 1
            compare_array = [rnd.randint(-100, 100) for _ in range(n)]
            my_sorting_array = compare_array[:]
            sorting_array = sorted(compare_array)
            self.sorting[self.name](my_sorting_array)

            str_i = f'0{i}' if i < 10 else str(i)
            print(f'\033[33mTEST №{str_i}----------')
            if sorting_array == my_sorting_array:
                print('\033[32m--------OK--------')
            else:
                print('\033[31m------FAILED------')
                failed_tests += f'\nWrong answer in the test №{str_i}:\n' \
                                f'Array: {compare_array}\n' \
                                f'Sorted array by Python: {sorting_array}.\n' \
                                f'Sorted array by function: {my_sorting_array}.\n'

        print('\033[0m------------------')
        print('---END TESTING----')
        print('------------------')
        if failed_tests:
            print(f'\n\033[1m\033[4mAdditionally:\n\033[0m\033[31m{failed_tests}\033[0m')
        print()

    def execute(self, a: list) -> None:
        if not self.name:
            print('\033[31mYou should choose the algorithm!\033[0m\n')
            return

        if self.name in self.sorting:
            self.sorting[self.name](a)
        else:
            raise SortingNameError


def comb_sort(a: list) -> None:
    if not isinstance(a, list):
        raise ListParameterError

    n = len(a)
    factor = 1.247
    step = n - 1

    while step >= 1:
        for i in mp.frange(n - step):
            if a[i] > a[i + step]:
                a[i], a[i + step] = a[i + step], a[i]
        step = int(step // factor)

    for _ in range(2):
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]


def gnome_sort(a: list) -> None:
    if not isinstance(a, list):
        raise ListParameterError

    n = len(a)
    i, j = 1, 2
    while i < n:
        if a[i - 1] <= a[i]:
            i, j = j, j + 1
        else:
            a[i - 1], a[i] = a[i], a[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1


# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[].
# n - размер кучи
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера


def heap_sort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап
        heapify(arr, i, 0)
