# Note that this algorithm works only with
# positive integers!


def counting_sort(array: list):
    frequency_list = [0 for _ in range(max(array)+1)]

    for i in range(len(array)):
        frequency_list[array[i]] += 1

    result = list()

    for i in range(len(frequency_list)):
        for j in range(frequency_list[i]):
            result.append(i)

    return result
