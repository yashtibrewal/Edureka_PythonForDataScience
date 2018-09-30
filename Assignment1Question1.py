#1.Write a program which will find factors of given number and find whether
#the factor is even or odd.Hint: Use Loop with if-else statements

input_number = input("Enter the number ")
input_number = int(input_number)
factors = []
for integer in range(2, input_number):
    if(input_number%integer==0):
        factors.append((integer,integer%2==0))

print("(Factors, Even) :",factors)
