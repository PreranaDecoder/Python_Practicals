#P7 Q.6 To find tuples which have all elements divisible by k from list of tuple.


M = []
N = int(input("Enter the value of N: "))
for i in range(0, 50):
    if i % N == 0:
        M.append(i)
M=tuple(M)
print("Tuple of numbers divisible by ", N)
print(M)

