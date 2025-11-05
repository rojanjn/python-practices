cost = int(input())

if cost > 50000:
    finalCost = cost - (cost * 0.2)
elif 20000 < cost < 50000:
    finalCost = cost - (cost * 0.1)
else:
    finalCost = cost
    
print(int(finalCost))