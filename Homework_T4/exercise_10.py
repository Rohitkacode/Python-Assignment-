def check_even(number):
    if number % 2 == 0:
            return True  
    else:
        return False
    

even_number = list(filter(check_even, range(1,21)))

print(even_number)