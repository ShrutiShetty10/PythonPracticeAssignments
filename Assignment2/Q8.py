'''
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
words=input("Enter words\n").split(",")
words.sort()
print("Sorted words are ")
print(words)

'''
OUTPUT
Enter words
without,hello,bag,world
Sorted words are 
['bag', 'hello', 'without', 'world']
'''