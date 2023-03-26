list = [-9, 2, 3, 4, 20, -28, 89, 8, 9,]
largest = list[0]
smallest =list[0]
for i in list:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
    
print("The largest number is : ", largest)
print("the smallest number is : ", smallest)


