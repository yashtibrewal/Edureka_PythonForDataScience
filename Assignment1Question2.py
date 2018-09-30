# 2.Write a code which accepts a sequence of words as input and prints
# the words in a sequence after sorting them alphabetically.
# Hint: In case of input data being supplied to the question,
# it should be assumed to be a console input.

input_String = input("Enter the sequence of words ")
input_String = input_String.split(" ")
print(input_String)
input_String.sort()
print(input_String)
