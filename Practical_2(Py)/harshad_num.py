# PP-2 5) determine whether given number is harshad number or not
number = int(input('Enter number: '))

# Making copy of number for later use
copy = number

# Finding sum of digit
digit_sum = 0

while number:
    digit_sum += number%10
    number //= 10

# Checking divisibility & making decision
if copy%digit_sum == 0:
    print('%d is Harshad Number' % (copy))
else:
    print('%d is Not Harshad Number' % (copy))