# 5.Design a code which will find the given number is Palindrome number or not.
# Hint: Use built-in functions of string.

input_String = input("Enter a number: \n")
if input_String == input_String[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
