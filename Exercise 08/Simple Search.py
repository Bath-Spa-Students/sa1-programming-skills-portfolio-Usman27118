'''write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.'''

# Initialize list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Let the user input the NAME to search
SEARCH_NAMES = input("Enter the name you want to search for: ")

# Search NAME in list
if SEARCH_NAMES in names:
    print(f"{SEARCH_NAMES} is in the list.")
else:
    print(f"{SEARCH_NAMES}  not in the list.")
    
