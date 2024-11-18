#Exercise 9
'''Fill in the blanks in the code below so that the function hello() prints “Hello”
to the console.

def hello():
____ # Fill in this blank to print "Hello" to the console
def main():
____ # Fill in this blank to call the hello() function
if __name__ == "__main__":
main()'''

#void function
def hello(): #this function will print "Hello" to the console if called
    print('Hello')


def main(): #This is another function where we call the previous function
    hello()

#This function will ensure that the main() will be called only if it is executed directly
if __name__ == "__main__":
    main()