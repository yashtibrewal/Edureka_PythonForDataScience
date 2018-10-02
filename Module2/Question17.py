# 17.By using list comprehension, please write a program to
# print the list after removing delete numbers which are divisible
# by 5 and 7 in [12,24,35,70,88,120,155].
a = [12,24,35,70,88,120,155]
a = [i for i in a if i % 7 is not 0 and i % 5 is not 0]
print(a)
