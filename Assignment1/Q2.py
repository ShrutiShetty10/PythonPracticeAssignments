'''
Print the user input table
2*1 = 2
2*2 =4

'''
no=int(input("Enter the number for its multiplication table\n"))
for i in range(1,11):
    print(no,"*",i,"=",no*i)