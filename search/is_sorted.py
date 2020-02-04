
def is_sorted(array: list, *, least_to_greatest=True):
    flag = 2 * int(least_to_greatest) - 1  # 1 or -1

    for i in range(len(array)-1):
        if flag * array[i] > flag * array[i+1]:
            return False

    return True

