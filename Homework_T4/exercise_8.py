def question_8():
    squares = []  
    for i in range(1, 21):
        squares.append(i ** 2)  
    print(tuple(squares) )
    


# Or 

def que_8():
    squares = tuple(i ** 2 for i in range(1, 21))
    print(squares)
    



question_8()
que_8()