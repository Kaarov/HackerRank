for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        ans = a / b
        print(int(ans))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

# Done ✅
