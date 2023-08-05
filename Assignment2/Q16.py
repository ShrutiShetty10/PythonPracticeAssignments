'''
Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''

input_nos=input("Enter numbers\n").split(",")
print("Odd numbers are")
for i in input_nos:
    if int(i)%2==1:
        print(i,end=",")
'''
OUTPUT
Enter numbers
1,4,5,6,78,77,90
Odd numbers are
1,5,77,
'''