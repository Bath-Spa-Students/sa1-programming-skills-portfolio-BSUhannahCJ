#exercise 3 - Biography
#Advanced requirements

'''### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?'''

print("Create a biography!") #display message to ask user to create biography

#asks user for appropriate input
user_name = input('Enter your full name please: ')
user_hometown = input('Enter your home-town please: ')
user_age = input('Enter your age please: ')

#program to check whether or not the input entered for age is a digit or not
while not user_age.isdigit():
    print("Please enter your age in digits.") #will display if input is not a digit
    user_age = input("Enter your age please: ")

#dictionary for user's input
user_biography = {'Name' : user_name,
                  'Home-town' : user_hometown,
                  'Age' : user_age}

#finishing display message and print concatenation of the user's keys and values 
print("\nHere is your biography.")
print("Name:", user_biography["Name"], "\nHome-town:", user_biography["Home-town"], "\nAge:", user_biography["Age"])

