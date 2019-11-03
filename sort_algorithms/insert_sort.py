
def insert_sort(array: list):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array[j], array[i] = array[i], array[j]

    return array
