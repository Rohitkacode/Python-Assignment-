user_id = input("Please enter your user id: ")
user_password = input("Please enter your password: ")
user_confirm = input("Please enter your password again: ")
attemps = 0

for i in range(2):

    if user_password == user_confirm:
        print("Thank you , you are logged in")
        break
        
    else:
        user_confirm =input("Passwords do not match. Please try again : ")
        attemps += 1
        if attemps == 2:
            print("Sorry, you have tried 3 times")
            break
    
