
def shaker_sort(array: list):
    left = 0
    right = len(array)

    while right - left > 1:
        for i in range(right-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        right -= 1

        for j in range(right, left, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
        left += 1

    return array
