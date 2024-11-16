'''Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.'''

# Code to define the days in each month (default for non-leap years)
days_in_month = {
   1: 30,   #Month=January
    2: 28,   #Month=February
    3: 31,   #Month=March
    4: 30,   #Month=April
    5: 31,   #Month=May
    6: 30,   #Month=June
    7: 31,   #Month=July
    8: 31,   #Month=August
    9: 30,   #Month=September
    10: 31,  #Month=October
    11: 30,  #Month=November
    12: 31   #Month=December3
}

# Function to get number of days in a single month
try:
    # Enter the month number
    month = int(input("Enter the month number (1-12): "))
    
    # Valid the month number
    if month < 1 or month > 12:
        print("Invalid month number. Please enter a number between 1 and 12.")
        exit()
    # Examine if the month is February and handle leap year
    if month == 2:
        # Interrogate if it's a leap year
        leap_year = input("Is it a leap year? (yes or no): ").strip().lower()
        if leap_year == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days in a non-leap year.")
    else:
        # Code to output the number of days for determine month
        print(f"The month {month} has {days_in_month[month]} days.")

except ValueError:
    print("Invalid input . Please enter a number.")
