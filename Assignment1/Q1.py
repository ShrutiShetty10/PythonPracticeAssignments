#create one empty list add prime nos to the list 50
import math
list=list()
flag=False
print("Prime numbers are")
for n in range(0,50):
    if n<=1:
        continue
   
    for i in range(2,n):
        if n%i==0:
            break
    else:
        list.append(n)
print(list)     

'''
Output
Prime numbers are
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
'''