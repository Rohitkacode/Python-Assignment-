input_string = input("Enter a String : ")
number = 0
string = 0
for i in input_string :

    try:
        int(i)
        number+=1
    except ValueError:
        string+=1

print("Letters: ", string, " Digits: ", number)






