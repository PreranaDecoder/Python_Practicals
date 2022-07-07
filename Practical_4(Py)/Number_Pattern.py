n=4
num=1
for i in range(1,n+1):
    for num in range(1,i+1):
        print(num,"*",end="")
    num+=1
    print()