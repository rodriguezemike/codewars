#Cached
def fibonacci(n, cache = {0:0, 1:1}):
    if n in cache:
        return cache[n]
    else:
        fibonacci(n-1, cache)
        cache[n] = cache[n-1] + cache[n-2]
        return cache[n]

#memoized
def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci_mem(n):
    if n in [0, 1]:
        return n
    return fibonacci_mem(n - 1) + fibonacci_mem(n - 2)

#with lru_cache
from functools import lru_cache

@lru_cache(None)
def fibonacci_lru_cache(n):
    if n in [0, 1]:
        return n
    return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)

