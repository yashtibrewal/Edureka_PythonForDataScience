# 3.Write a program, which will find all the numbers between 1000 and 3000
# (both included) such that each digit of a number is an even number.
# The numbers obtained should be printed in a comma separated sequence
# on a single line.Hint: In case of input data being supplied to the question,
# it should be assumed to be a console input.Divide each digit with 2 and
# verify is it even or not.

numbers = []
for i in range(1000, 3001, 2):
    j = i
    even = False
    while j > 0:
        if j % 2 == 0:
            j //= 10
            even = True
        else:
            even = False
            break
    if even:
        numbers.append(i)
print(numbers)
