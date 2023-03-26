from functools import reduce

input_list = [1, 2, 3, 4, 5, 6, 7,]

result = reduce(lambda x, y: str(x) + str(y), input_list)


print("Flattened string is : ", result)
