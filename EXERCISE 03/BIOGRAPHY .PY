'''In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.'''


# Step 1: Define the information as variables
name = "Usman"
hometown = "Ras Al Khaima"
age = 24

# Step 2: Create a dictionary to store the information
userinfo1 = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Step 3: Print the values on separate lines using a single print statement
print(f"Name: {userinfo1['name']} \nHometown:  {userinfo1['hometown']} \nAge: {userinfo1['age']}")
