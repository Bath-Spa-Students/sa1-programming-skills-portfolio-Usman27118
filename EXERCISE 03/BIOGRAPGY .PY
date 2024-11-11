'''In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.'''


#Define the information as variables
Name = "Muhammad Usman"
Hometown = "Ras Al Khaimah"
Age = 22

#Create a dictionary to store the information
userinfo1 = {
    "Name": Name,
    "Hometown": Hometown,
    "Age": Age
}

# Print the values on separate lines using a single print statement
print(f"Name: {userinfo1['Name']} \nHometown:  {userinfo1['Hometown']} \nAge: {userinfo1['Age']}")
