'''
       *
      * *
     * * *
    * * * *
     * * *
      * *
       *
'''

n=4
spaces=n-1

for i in range(1,n+1):
    print(" "*spaces,end="")
    for j in range(i):
        print("*",end=" ")
    spaces-=1
    print()

spaces=n-(n-1)
for q in range(1, n):
    print(" " * spaces, end="")

    for p in range(1,n):
        print("* ", end="")

    spaces += 1
    n -= 1
    print()
