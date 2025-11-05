def skyline(*args):
    if not args:
        return 0
    return max(args)
        
heights = list(map(int, input().split()))
print(skyline(*heights))