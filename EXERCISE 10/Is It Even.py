'''Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.'''

def is_even(number):
    return number % 2 == 0

def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print("The number is even.")
    else:
        print("The number is odd.")

#if_name_ == "_main_":
main()
