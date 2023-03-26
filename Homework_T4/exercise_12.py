def divide(i):
    try:
        result = 5/i
        print(result)
    except ZeroDivisionError:
        print("Cannot devide by 0")

divide(0)



