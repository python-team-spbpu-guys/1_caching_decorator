from functools import wraps
from collections import OrderedDict


def cache_decorator(cache_depth=10):
    """
    Caching decorator that stores the results of function executions.

    Parameters:
    cache_depth: maximum number of stored results for each function.
    """

    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                return cache[key]

            result = func(*args, **kwargs)
            cache[key] = result

            if len(cache) > cache_depth:
                cache.popitem(last=False)

            return result

        return wrapper

    return decorator
