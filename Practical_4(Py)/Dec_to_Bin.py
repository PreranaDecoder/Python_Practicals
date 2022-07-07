# P4 (Q.2) - Python program to convert number Decimal to Binary.

def Dec_to_Bin(num):
    if num > 1:
        Dec_to_Bin(num//2)
    print(num%2 , end="")

num = int(input("Enter Decimal number : "))
Dec_to_Bin(num)