numbers = [-1, 0, 1, 2, -1, -4]

# numbers = list(set(numbers))
numbers.sort()
print(numbers)
for index, element in enumerate(numbers):

    if index != 0 and element == numbers[index - 1]:
        continue

    a = index + 1
    b = len(numbers) - 1

    while a < b and a != b:

        suma = element + numbers[a] + numbers[b]

        if suma == 0:
            print([element, numbers[a], numbers[b]])

        if suma > 0:
            b -= 1
        else:
            a += 1
