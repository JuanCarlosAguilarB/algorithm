array = [6, 5, 3, 1, 8, 7, 2, 4]


def array_sort(array):
    length = len(array)

    for i in range(2, length):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
            j -= 1
            print(array)


array_sort(array)
