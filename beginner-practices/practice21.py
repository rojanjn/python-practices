import time

def timing(func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper

@timing
def my_list(n):
    return list(range(1, n + 1))

n = int(input())
print(my_list(n))