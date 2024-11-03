from decorator import cache_decorator


@cache_decorator(cache_depth=3)
def add(a, b):
    return a + b


@cache_decorator(cache_depth=2)
def multiply(a, b):
    return a * b


def test_add_caching():
    assert add(2, 3) == 5  # First call, calculates and caches
    assert add(2, 3) == 5  # Cached result
    assert add(4, 5) == 9  # Different arguments, calculates and caches
    assert add(2, 3) == 5  # Should still be cached


def test_cache_depth_limit():
    assert add(1, 1) == 2  # Caches (1, 1) -> 2
    assert add(2, 2) == 4  # Caches (2, 2) -> 4
    assert add(3, 3) == 6  # Caches (3, 3) -> 6, reaches depth limit
    assert add(4, 4) == 8  # Caches (4, 4) -> 8, evicts (1, 1)

    # Verify that (1, 1) was evicted from the cache
    assert add(1, 1) == 2  # Recomputes as it was evicted


def test_independent_caches_for_functions():
    # Testing add function cache
    assert add(5, 5) == 10  # Calculates and caches
    assert add(5, 5) == 10  # Cached result

    # Testing multiply function cache, with separate cache depth limit
    assert multiply(5, 5) == 25  # Calculates and caches
    assert multiply(5, 5) == 25  # Cached result
    assert multiply(3, 3) == 9  # Calculates and caches
    assert multiply(4, 4) == 16  # Caches, evicts (5, 5) due to cache depth limit


def test_cache_different_arguments():
    # Different arguments should result in different cache entries
    assert add(2, 3) == 5
    assert add(3, 2) == 5  # Different key due to argument order
    assert add(2, 3) == 5  # Cached
