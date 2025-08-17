def pick_evens(*args):
    evens = []

    for i in args:
        if i % 2 == 0:
            evens.append(i)
    return evens
        
nums = list(map(int, input().split()))
print(pick_evens(*nums))