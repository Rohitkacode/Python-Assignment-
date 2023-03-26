# Exercise 2 by Rohit Bokil

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def avg(n1,n2, n3,n4):
    return (n1+n2+n3+n4)/4

def check_negative(n):
    if n < 0:
        return "it's a Negative number"
    else:
        return "it's not a Positive number"


user_input = int(input('''Enter 1 - Addition
Enter 2 - Subtraction
Enter 3 - Division
Enter 4 - Multiplication
Enter 5 - Average
Enter your choice: '''))

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

Final_answer = 0

if user_input == 5:
    num3 = int(input('Enter third number: '))
    num4 = int(input('Enter fourth number: '))

if user_input == 5:
    Final_answer =avg(num1,num2, num3,num4)

if user_input == 1:
    Final_answer =add(num1,num2)


if user_input == 2:
    Final_answer =subtract(num1,num2)

if user_input == 3:
    Final_answer =divide(num1,num2)

if user_input == 4:
    Final_answer =multiply(num1,num2)


is_negative = check_negative(Final_answer)
print(f"Your answer is {Final_answer} and {is_negative}")

        





