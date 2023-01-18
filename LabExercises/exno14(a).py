try:
    print("Enter the first number")
    a=int(input())
    print("Enter the second number")
    b=int(input())
    c=a/b
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
