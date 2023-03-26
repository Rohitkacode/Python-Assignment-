secret_number = 12
counter =1
while counter <= 5:
    user_guess = input("Guess a number")
    counter += 1

    if int(user_guess) == secret_number:
        print("Good Guess!")

    elif counter > 5:
        print("Game Over!")
        
    else:
        print("Try Again!")




