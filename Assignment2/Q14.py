'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lo case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
input_str=input("Enter input\n")
up=0
lo=0
for i in range(len(input_str)):
    if input_str[i].isupper():
        up=up+1
    elif input_str[i].islower():
        lo=lo+1
    
print("UPPER CASE ",up)
print("LOWER CASE ",lo)

'''
OUTPUT
Enter input
I'm ShrutiShetty
UPPER CASE  3
LOWER CASE  11
'''