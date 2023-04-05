
import math
C = 50
H = 30

D = input("Enter thr digits in comma-separated sequence : ").split(",")

for i in D:
    Q = math.sqrt((2*C*int(i))/H)
    print(Q)

