# 16.By using list comprehension, please write a program to
# print the list after removing the 0th,4th,5th numbers in
# [12,24,35,70,88,120,155].

a = [12,24,35,70,88,120,155]
a.remove(12)
a.remove(88)
a.remove(120)
a = [i for i in a]
print(a)

