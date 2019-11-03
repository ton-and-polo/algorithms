from random import randint


def quick_sort(array: list):
    # Tony Hoare sort.
    if len(array) == 1:
        return array

    break_point = array[randint(0, len(array)-1)]

    less = list()
    bigger = list()
    equal = list()

    for i in array:
        if i < break_point:
            less.append(i)
        elif i > break_point:
            bigger.append(i)
        else:
            equal.append(i)

    return quick_sort(less) + equal + quick_sort(bigger)
