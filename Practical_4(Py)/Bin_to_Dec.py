# P4 (Q.2) - Python program to convert number Binary to Decimal.

def Bin_to_Dec(num):
    return int(num , 2)

num = str(input("Enter Binary number : "))
print("Decimal number :", Bin_to_Dec(num))