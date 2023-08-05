'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
input_list=input("Enter numbers for factorial\n").split(" ")

def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)
print("The factorial of entered numbers are") 
for i in input_list:
    ans=fact(int(i))
    print(ans,end=",")

'''
OUTPUT
Enter numbers for factorial
8 10 5
The factorial of entered numbers are
40320,3628800,120,
'''