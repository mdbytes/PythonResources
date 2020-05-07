try:
    a = input("enter a number")
    b = input("enter another number")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Invalid Input")
    
