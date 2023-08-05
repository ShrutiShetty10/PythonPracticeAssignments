'''
Printing palindrome string
Take input as the word is Madam =>Malayalam
'''
import math
word=input("Enter word to check if its a palindrome\n")
word=word.lower()
flag=True
for i in range(0,math.ceil(len(word)/2)):
    if word[i]!=word[len(word)-1-i]:
        flag=False
        print(word," is not a palindrome")
        break
if flag:
    print(word," is a palindrome")