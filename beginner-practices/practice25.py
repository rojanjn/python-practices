def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    
while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = division(num1, num2)
        
        if result is not None:
            print("Result:", result)
            break
        
    except ValueError:
        print("Error: You can only input integers!")

    finally:
        print("\nبرنامه به موفقیت اجرا شد!")
