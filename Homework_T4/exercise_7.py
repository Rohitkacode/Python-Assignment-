def max_lenght(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    
    else:
        print(f"{str1}\n{str2}")

max_lenght("hello", "hello")