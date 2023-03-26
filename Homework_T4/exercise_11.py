inputlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_list = filter(lambda x: x % 2 == 0, inputlist)

squares_list = map(lambda x: x ** 2, filtered_list)

final_list = list(squares_list)


print(final_list)
