# Write a program to check if the given number is a palindrome number.

# Pseudocode

def palindrome(number):
# Convert the number to a word
    string_number = str(number)
# reverse and check if it is still equal
    return string_number == string_number[::-1]
# code for users input
user_input = int(input("Enter a number: "))
# if-else statement
if palindrome(user_input):
    print(f"the original number is {user_input}")
    print(f"Yes. given number {user_input} is palindrome number")
else:
    print(f"the original number is {user_input}")
    print(f"No. given number {user_input} is not palindrome numbe")