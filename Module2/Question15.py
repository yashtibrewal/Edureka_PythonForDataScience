# 15.By using list comprehension, please write a program to print
# the list after removing the value 24 in [12,24,35,24,88,120,155].
a = [12,24,35,24,88,120,155]
a = [i for i in a if i is not 24]
print(a)
