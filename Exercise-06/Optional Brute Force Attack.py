'''## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345.
 The program should keep asking the user to enter the password until they provide the correct one.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, 
inform them of the remaining attempts. If the maximum number of attempts is reached, 
inform the user that the authorities have been alerted.'''

#Exercise 6 - Brute Force Attack
#optional requirements 

the_correct_password = "12345" #variable with the correct password
attempts_allowed = 5 #max amount of attempts allowed
user_attempts = 0 #attempts user starts with

while user_attempts < attempts_allowed: #user has 5 attempts and the loop will continue until attempts run out or user enters the correct password
    password_entered = input("Enter password: ")
    if password_entered == the_correct_password:
        print("Access granted. Welcome!")
        break # loop breaks once the correct password is entered
    else: #if else the user continues to get it wrong, the loop will continue until attempts run out
        user_attempts += 1
        attempts_left = attempts_allowed - user_attempts
        if attempts_left > 0:
            print ("Incorrect password. you have " + str(attempts_left) + " attempts left. Try again.")
        else:
            print("Incorrect password. Shutting down. Authorities have been alerted.") #once the attempts have reach the max, this will print out

