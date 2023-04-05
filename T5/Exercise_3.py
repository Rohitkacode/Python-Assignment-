
try:
    user_input = int(input("Enter a number a 4 digit number: ")) 
    if len(str(user_input)) > 4:
        print("The length is too long!!! Please provide only four digits")
    elif len(str(user_input)) < 4:
        print("The length is too short!!! Please provide only four digits")

except ValueError:
    print("please provide only digits")

