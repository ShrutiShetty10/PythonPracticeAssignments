'''
Take input as a string and reverse it
First=>tsriF
'''
input_string=input("Enter a word to reverse it\n")
print("Reverse of the entered word is")
for i in range(len(input_string)-1,-1,-1):
    print(input_string[i])
