'''Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.'''

def is_even(num):
    return num % 2 == 0

def main():
    num = int(input("Enter a num: "))
    if is_even(num):
        print("The num is even.")
    else:
        print("The num is odd.")

#if_name_ == "_main_":
main()