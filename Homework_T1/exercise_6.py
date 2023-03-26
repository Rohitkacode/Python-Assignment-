#   since input function will only take the values in strings we cannot just go  with Type() function to determine value as it will always give string as output

a = input("Enter any value : ")
try:
    val = int(a)
    print("The data type of the input value is Integer")
    
except ValueError:
    try:
        val = float(a)
        print("The data type of the input value is a Float")
        
    except ValueError:
            print("The data type of the input value is String")
