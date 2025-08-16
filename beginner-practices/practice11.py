n = int(input())

if n % 5 == 0 and n % 3 == 0:
    print("n is divisible by 5 and 3")
elif n % 5 == 0:
    print("n is divisible by 5")
elif n % 3 == 0:
    print("n is divisible by 3")
else:
    print("n is not divisible by 5 or 3")