# ascending order sorter

# Insertion sort

import sys
import re
import random
import os
import math
test_case = [5, 2, 4, 6, 1, 3]


def array_sort_1(base_array):
    # we make a copy of the array to avoid changing the original array,
    # because python is pass by reference
    array = base_array.copy()
    print('-----------------------------------------')
    print('base case', array)
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            aux = array[j-1]
            array[j-1] = array[j]
            array[j] = aux
            # print(array)
            j -= 1

    print('sorting array 1', array)
    print('-----------------------------------------')
    return array


def array_sort_2(base_array):
    array = base_array.copy()
    print('-----------------------------------------')
    print('base case', array)

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    print('sorting array 2', array)
    print('-----------------------------------------')
    return array


array_sort_1(test_case)
array_sort_2(test_case)

page 19
https: // cdn.manesht.ir/19908___Introduction % 20to % 20Algorithms.pdf


#!/bin/python3


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def is_open(char):
    return char in '{[('


def isBalanced(s):
    stack = []
    for i in s:
        if is_open(i):
            stack.insert(0, i)
        else:
            if len(stack) == 0:
                return 'NO'

            string = stack.pop(0) + i
            if not string in ['()', '[]', '{}']:
                return 'NO'

    return 'YES' if len(stack) < 1 else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
