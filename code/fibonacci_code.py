cache = {}
cache[0]=0
cache[1]=1
def fib(n):
    if n in cache:
        return cache[n]
    else:
        result = fib(n-1) + fib(n-2)
        cache[n] = result
        return result
