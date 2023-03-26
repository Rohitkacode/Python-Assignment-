numbers = range(1000)

result = list(filter(lambda x: (x % 3 != 0 and x % 7 == 0), numbers))

print(result)