user_input = input("Enter a sequence of comma-separated numbers :")
list = user_input.split(",")
tuple = ()

for i in list:
    tuple += (i,)

print("Tuple : ", tuple)
print("List: ", list)