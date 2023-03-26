list_1 =[1,3,5,7,9,10,]
list_2 =[2,4,6,8]

list_1[-1] = list_2[0]
for i in range(1,len(list_2)):
    list_1.append(list_2[i])

print(list_1)

