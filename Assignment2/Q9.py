'''
Question:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
sentences=list()
print("Enter sentences")
while True:
    user_input = input()

   
    if user_input == '':
        break
    else:
        sentences.append(user_input + '\n')

for s in sentences:
    print(s.upper())
'''
OUTPUT
Enter sentences
Hello world
Practice makes perfect

HELLO WORLD

PRACTICE MAKES PERFECT
'''