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
            'selection': selection_sort
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
    swaps = True
    step = n

    while step > 1 or swaps:
        swaps = False
        step = int(step / factor)
        if step < 1:
            step = 1

        for i in range(n - step):
            j = i + step
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                swaps = True


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


def selection_sort(a: list) -> None:
    if not isinstance(a, list):
        raise ListParameterError

    n = len(a)

    for i in range(n // 2):
        max_ind = i
        min_ind = i
        for j in range(i, n - i):
            if a[j] > a[max_ind]:
                max_ind = j
            if a[j] < a[min_ind]:
                min_ind = j

        a[max_ind], a[n - i - 1] = a[n - i - 1], a[max_ind]
        if min_ind == n - i - 1:
            min_ind = max_ind
        a[min_ind], a[i] = a[i], a[min_ind]
