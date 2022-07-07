# PP-2 3) Write a python program to check if the given number is Disarium number.
#          exp., 1^1+7^2+5^3 = 175

def calculateLength(n):
    length = 0
    while (n != 0):
        length = length + 1
        n = n // 10
    return length

num = int(input("Enter the number : "))
rem = sum = 0
len = calculateLength(num)

n = num

while (num > 0):
    rem = num % 10
    sum = sum + int(rem ** len)
    num = num // 10
    len = len - 1

if (sum == n):
    print(str(n) + " is a disarium number")
else:
    print(str(n) + " is not a disarium number")











