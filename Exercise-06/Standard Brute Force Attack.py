#Exercise 6 - Brute Force Attack
#Standard requirements 

'''Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

'''

the_correct_password = "12345" #variable with the correct password
while input("Enter password: ") != the_correct_password: #while loop + input command. If the password entered is not equal to the correct password v
    print("Incorrect password. Try again.") #this output will be printed
print("Access granted. Welcome!") #if the correct password is entered, this output will be printeed.