# 6) Find transpose of the matrix.
x = [[11,12,13],
    [21,22,23],
     [31,32,33]]
res = [[0,0,0],
       [0,0,0],
       [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        res[j][i] = x[i][j]
for trans in res:
    print(trans)
