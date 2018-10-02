# 18.Please  write  a  program  to  randomly  generate  a  list  with
# 5  numbers,  which  are divisible by 5 and 7 , between 1 and 1000 inclusive.
import random
a = [i for i in range(1, 1000)]
random_numbers = []
while len(random_numbers) < 5:
    digit = random.choice(a)
    if digit % 5 is 0 and digit % 7 is 0:
        random_numbers.append(digit)
print(random_numbers)
