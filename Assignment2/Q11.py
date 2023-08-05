'''
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
num = [x for x in input("Enter binary numbers\n").split(',')]
print("Numbers divisible by 5 are")
for n in num:
    x = int(n, 2)
    if x%5==0:
        print(n)
        
'''
OUTPUT
Enter binary numbers
0100,0011,1010,1001
Numbers divisible by 5 are
1010
'''