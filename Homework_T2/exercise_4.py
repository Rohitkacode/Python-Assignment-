#exercise_4 by Rohit Bokil

will_continue = True
while will_continue:
    input_number = int(input("Enter a number: "))

    if input_number < 0:
        print("It's Over")
        will_continue = False
    elif input_number >= 0:
        print("Good going")    



