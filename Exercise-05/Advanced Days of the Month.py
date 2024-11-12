'''Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
'''

#exercise 5
#Days of the Month - advanced requirements

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
# if input is 2(feb) then it will ask for the year
if Month_user == 2:
    year_input = int(input("Which year? : "))
    if (year_input % 4 == 0):  #check if divisible by 4 because leap year is every 4 years
        Months_and_days['2'] = '29'  #if leap year then value will change

#Will print the days in given month if it is from 1-12
if STRMonth_user in Months_and_days:
    print(Months_and_days[STRMonth_user], "days.")
else:
    print("Invalid. Must be from 1-12") #else this will print