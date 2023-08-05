'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''
class Test:
    
    def __init__(self) -> None:
        self.testStr=""
        

    def getString(self):
        self.testStr=input("Enter input string\n")
        
    def printString(self):
        print("Entered string is\n",self.testStr.upper())

              
def main():
    obj=Test()
    obj.getString()
    obj.printString() 
if __name__ == "__main__":
    main()

'''
OUTPUT
Enter input string
Hello World!
Entered string is
 HELLO WORLD!
'''