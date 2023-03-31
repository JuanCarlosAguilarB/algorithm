
test_case = [5, 2, 4, 7, 1, 3, 2, 6]


def merge_sort_resursion(base_array):

    if len(base_array) <= 1:
        return base_array

    middle_inedx = len(base_array) // 2
    left_array = merge_sort_resursion(base_array[:middle_inedx])
    right_array = merge_sort_resursion(base_array[middle_inedx:])

    i, j = 0, 0
    sorted_array = []
    while i < len(left_array) and j < len(right_array):

        if left_array[i] <= right_array[j]:
            sorted_array.append(left_array[i])
            i += 1
        else:
            sorted_array.append(right_array[j])
            j += 1
        k = +1

    while i < len(left_array):
        sorted_array.append(left_array[i])
        i += 1
        k += 1

    while j < len(right_array):
        sorted_array.append(right_array[j])
        j += 1
        k += 1

    return sorted_array


print(test_case)
# merge_sort_resursion(test_case)
print(merge_sort_resursion(test_case))
