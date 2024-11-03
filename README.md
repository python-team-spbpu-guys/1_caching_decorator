
# Python Caching Decorator

This project provides a caching decorator that can be used to cache the results of functions to improve performance. The decorator is flexible and supports configuring the cache depth to limit the number of cached results.

## Project Structure

```
project_root/
├── decorator.py    # Contains the caching decorator 
└── test_decorator.py  # Contains pytest test cases for the decorator
```

## Features

- **Caching Decorator**: Stores the results of function executions, returning cached results for repeated calls with the same arguments.
- **Configurable Cache Depth**: Limits the number of results stored, evicting the oldest results first (FIFO) when the cache reaches its depth limit.
- **Supports Multiple Functions**: Multiple functions can be decorated simultaneously, each maintaining its own cache.

## Testing

The tests for this project are located in the `tests` folder and use `pytest`. Tests cover the following scenarios:

1. **Basic Caching**: Verifies that results are cached after the first computation.
2. **Cache Depth Limit**: Ensures that results are evicted once the cache depth limit is reached.
3. **Independent Caches for Different Functions**: Confirms that each decorated function maintains its own cache.
4. **Caching with Different Arguments**: Checks that results are cached independently based on arguments.

### Running Tests

1. Install `pytest` if you haven't already:

    ```bash
    pip install pytest
    ```

2. Run tests from the project root:

    ```bash
    pytest
    ```

## Configuration

You can configure the cache depth for each function by passing the `cache_depth` parameter to `cache_decorator`. For example:

```python
@cache_decorator(cache_depth=5)
def some_function(a, b):
    # function logic
    pass
```

## Setup

**Clone the repository**:
   ```bash
   git clone <repository_url>
   cd project_root
   ```

## Example Usage

```python
from decorator import cache_decorator


@cache_decorator(cache_depth=3)
def add(a, b):
    return a + b


@cache_decorator(cache_depth=2)
def multiply(a, b):
    return a * b


print(add(2, 3))  # Calculates and caches the result
print(add(2, 3))  # Returns the cached result
print(multiply(2, 3))  # Calculates and caches the result
```

## License

This project is open-source and free to use.
