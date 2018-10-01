#4.Write a program that accepts a sentence and calculate the number of
# letters and digits.Suppose if the entered string is: Python0325
# Then the output will be:
# LETTERS: 6
# DIGITS:4

input_String = input("Enter a sentence \n")
letter_counter = 0
digit_counter = 0
for element in input_String:
    if element.isdigit():
        digit_counter += 1
    elif element.isalpha():
        letter_counter += 1
print("Letters: ", letter_counter)
print("Digits: ", digit_counter)
