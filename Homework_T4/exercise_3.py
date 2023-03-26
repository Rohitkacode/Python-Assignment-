# we can also use set() function 

list = [1,1,2,2,3,3,7,9,66,8,8,2]

def unique_list(list):
    new_list =[]
    for i in list:
        if i not in new_list:
            new_list.append(i)

    return new_list

unique_list = unique_list(list)
print(unique_list)

    





