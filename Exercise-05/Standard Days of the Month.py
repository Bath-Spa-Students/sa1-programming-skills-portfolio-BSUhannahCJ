'''Exercise 5: Days of the Month - 30 Marks

Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

 Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
'''
#Days of the Month - standard requirements

#Dictionary with month numbers and the amount of days in that month
Months_and_days = {'1': '31',   # January
                   '2': '28',   # February
                   '3': '31',   # March
                   '4': '30',   # April
                   '5': '31',   # May
                   '6': '30',   # June
                   '7': '31',   # July
                   '8': '31',   # August
                   '9': '30',   # September
                   '10': '31',  # October
                   '11': '30',  # November
                   '12': '31'}  # December

#asking input from user
Month_user = int(input("Please enter the number of the month (1-12): "))

# converting it to a string data type in order to match with the dictionary
STRMonth_user = str(Month_user)

#Will print the days in given month if it is from 1-12
if STRMonth_user in Months_and_days:
    print(Months_and_days[STRMonth_user], 'days')
else:
    print("Invalid. Must be from 1-12") #else this will print