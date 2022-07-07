# Q.1 ) Python program to find list of list using recursion

listt = [1, 2, 3, 4, 5, 6]

if not listt:
    print(0)
else:
    print(1 + len(listt[1::2]) + len(listt[2::2]))

