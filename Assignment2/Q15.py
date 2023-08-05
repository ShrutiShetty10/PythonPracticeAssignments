'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
digit=input("Enter digit\n")
ans=int(0)
temp=digit
for i in range(1,4):
    temp=temp+digit
while len(temp)>0:
    ans=ans+int(temp)
    temp=temp[:len(temp)-1]
print("Output:",ans)
'''
OUTPUT
Enter digit
9
Output: 11106
'''

