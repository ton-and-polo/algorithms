

def binary_search(target, array: list):
    # Works only with sorted array.
    floor_index = -1
    celling_index = len(array)

    while floor_index + 1 < celling_index:
        guess_index = (celling_index + floor_index)//2
        if target == array[guess_index]:
            return True
        if target < array[guess_index]:
            celling_index = guess_index
        else:
            floor_index = guess_index

    return False

