n = int(input())
x = int(input())

for i in range(n):
    if x % 2 == 1:
        x = x * 2 - 1
    else:
        x = x // 2
        
print(x)