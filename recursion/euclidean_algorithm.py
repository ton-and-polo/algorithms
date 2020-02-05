
def num_calls(function):
    # A simple decorator that counts how many
    # times the function was called.
    def wrapper(*args):
        wrapper.counter += 1
        return function(*args)
    wrapper.counter = 0
    return wrapper


@num_calls
def gcd(x, y):
    if x == y:
        return x

    if x < y:
        return gcd(x, y-x)
    return gcd(x-y, y)


@num_calls
def gcd_improved(x, y):
    if y == 0:
        return x
    return gcd_improved(y, x % y)


x = 100
y = 6

print(f'GCD({x}, {y}): {gcd(x, y)}, num_calls: {gcd.counter}.')
print(f'GCD_improved({x}, {y}): {gcd_improved(x, y)}, num_calls: {gcd_improved.counter}.')