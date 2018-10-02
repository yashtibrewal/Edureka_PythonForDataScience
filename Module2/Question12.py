# 12.Please write a program which count and print the numbers of
# each character in a string input by console.
# Example: If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2c,2b,2e,1d,1g,1f,1


user_input = input("Enter the string:\n")
unique_elements = set(user_input)
for element in unique_elements:
    print(user_input.count(element),element)
