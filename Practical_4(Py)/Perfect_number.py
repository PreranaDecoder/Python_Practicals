# P4 (Q.1) - Python program to Print Perfect Number.

# Sum of factors equal to given number.
# num = 28
# 28 is perfect number.

num = int(input("Enter any number - "))
factor = []
for i in range(1,num):
    if num%i == 0:
        factor.append(i)
summ = sum(factor)
if summ == num:
    print(num,"is a Perfect Number.")
