
def cache(function):
    # A simple decorator that caches
    # the result of the function.
    def wrapper(*args):
        if args not in wrapper.cache:
            wrapper.cache[args] = function(*args)
        return wrapper.cache[args]

    wrapper.cache = dict()
    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return 0 if n == 0 else 1
    return fibonacci(n-1) + fibonacci(n-2)

