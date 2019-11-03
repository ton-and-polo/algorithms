
def merge_sort(array: list):
    if len(array) == 1:
        return array

    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])

    merged_list = list()

    # Pointers:
    pointer_left = 0
    pointer_right = 0

    while pointer_left < len(left) and pointer_right < len(right):
        if left[pointer_left] <= right[pointer_right]:
            merged_list.append(left[pointer_left])
            pointer_left += 1

        else:
            merged_list.append(right[pointer_right])
            pointer_right += 1

    if pointer_right == len(right):
        for i in range(pointer_left, len(left)):
            merged_list.append(left[i])
    else:
        for i in range(pointer_right, len(right)):
            merged_list.append(right[i])

    return merged_list
