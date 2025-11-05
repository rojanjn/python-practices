def sum_numbers(*args):
    if not args:
        return 0
    else:
        return sum(args)
    
nums = list(map(int, input().split()))
print(sum_numbers(*nums))