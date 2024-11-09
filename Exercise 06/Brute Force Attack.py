'''Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.'''

# this is the  password
password = "12345"

# total  attempts
tottal_atemps = 5

# num of attempts beginning
attempts = 0

# While loop to continiusly ask for the password
while attempts < tottal_atemps:
    # Ask the user to input the password
    entered_password = input("Enter the password: ")
    
    # Check if the entered password is correct
    if entered_password == password:
        print("Password correct! Access granted.")
        break
    else:
        # plus 1 to the attempts counter
        attempts += 1
        # Inform the user of the remaining attempts
        remaining_attempts = tottal_atemps - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Incorrect password. You have reached the maximum attemp")