import time


def timed(inner_func):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        inner_func(*args, **kwargs)
        end = time.time()
        print(f"Excuted {inner_func.__name__} {end - start:.3f} seconds")

    return wrapped_func


def cache_it(inner_func):
    memo = {}

    def wrapped_func(k):
        if k not in memo:
            memo[k] = inner_func(k)

        return memo[k]

    return wrapped_func


@cache_it
def fib(num):
    if num < 2:
        return 1

    return fib(num - 2) + fib(num - 1)


@timed
def help():
    print(fib(40))


if __name__ == "__main__":
    help()
