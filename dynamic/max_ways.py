
def max_ways(n, steps: list):
    ways_counter = [0 for _ in range(n+1)]
    # base case
    ways_counter[0] = 1

    for i in range(1, len(ways_counter)):
        for step in steps:
            if i >= step:
                ways_counter[i] += ways_counter[i - step]

    return ways_counter[n]


print(max_ways(10, [1, 2]))  # 89
