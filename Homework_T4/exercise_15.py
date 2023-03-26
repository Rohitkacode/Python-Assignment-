
List_of_numbers  = [1, 2, 3, 4, 5]

def multiply(num):
    return num * num

# use map() to apply the function to each element in the list
result = list(map(multiply, List_of_numbers))

print(List_of_numbers)
print(result)
