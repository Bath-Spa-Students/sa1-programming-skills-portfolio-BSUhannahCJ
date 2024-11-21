#exercise 10
'''Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.'''

#passing an argument through this function
def even_or_odd(NUM):
    if NUM % 2 == 0:  #simple code to check if number is even or odd
        print("It's an even number!")
    else:
        print("It's an odd number!")

#the main function where the program starts
def MAIN():
    number = int(input("Enter a number: ")) #asking input
    even_or_odd(number) #calling previous function 

#calling the function
if __name__ == "__main__":
    MAIN()
