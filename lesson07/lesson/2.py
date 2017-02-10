# -*- coding: utf-8 -*-
"""Малахов Максим."""
import time
from functools import wraps


def log(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        """Декоратор логирования."""
        res = func(*args, **kwargs)
        print("Log {}({}, {}) = {}").format(func.__name__, args, kwargs, res)
        return res
    # decorated.__name__ = func.__name__
    return decorated

def time_it(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        """Декоратор времени."""
        start = time.time()
        res = func(*args, **kwargs)
        delta = time.time() - start
        print("Function {} worked {}").format(func.__name__, delta)
        return res
    # decorated.__name__ = func.__name__
    # decorated.__doc__ = func.__doc__
    return decorated


def my_sum(a, b):
    """Суммирование."""
    return a + b


@log
@time_it
def my_mul(a, b):
    """Умножение."""
    return a * b


my_sum = log(my_sum)


res = my_mul(b=13, a=5)
print(res)

res = my_sum(6, 5)
print(res)

res = my_mul(6, 9)
print(res)

print(help(my_mul))
