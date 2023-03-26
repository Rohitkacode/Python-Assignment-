secret_number = 23

should_continue = True
while should_continue:
    number = int(input("Guess a number : "))

    if number == secret_number:
        print("You guessed it right!")
        should_continue = False
    else:
        answer= input("do you want to try again? (Yes/No) ").lower()
        if answer == "no":
            should_continue = False
            
