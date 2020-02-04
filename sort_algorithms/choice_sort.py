
def choice_sort(array: list):
    for i in range(len(array)-1):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array
