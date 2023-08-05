'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
input_str=input("Enter input\n")
letter=0
digit=0
for i in range(len(input_str)): 
    if input_str[i].isnumeric():
        digit=digit+1
    if input_str[i].isalpha():
        letter=letter+1

print("LETTERS ",letter)
print("DIGITS ",digit)
'''
OUTPUT
Enter input
I'm ShrutiShetty10
LETTERS  14
DIGITS  2
'''

