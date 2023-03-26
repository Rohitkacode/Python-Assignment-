#(i)
def foo():
    try:
     return 1
    finally:
     return 2
k = foo()
print(k)

#The finally block returns the value 2,
#which overrides the return value of 1 from try block.

#(ii) 
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()

#Ii will give NameError, because f(x, 4) is not defined,
#but finallly block will still print "afterf " "and afterf?"




