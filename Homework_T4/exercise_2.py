string = "Hello_World"

def count_upper_lower(s):
    upper, lower = 0, 0
    for i in string:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1

    print(f"No. of Uppercase characters : {upper} No. of Lower case Characters : {lower}")

count_upper_lower(string)

