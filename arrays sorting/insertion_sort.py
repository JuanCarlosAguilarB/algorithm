# ascending order sorter

# Insertion sort

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


