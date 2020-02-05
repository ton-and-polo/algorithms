
def min_price_way(n: int, steps: list, price: list):
    assert n <= len(price)-1, 'The amount of price elements should be n + 1.'

    price_counter = [0 for _ in range(n+1)]
    for i in range(1, len(price_counter)):
        previous_price = list()

        for step in steps:
            if i >= step:
                previous_price.append(price_counter[i-step])

        price_counter[i] = price[i] + min(previous_price)

    return price_counter[n]


print(min_price_way(3, [1, 2], [0, 10, 3, 5]))  # 8
