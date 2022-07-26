my_tuple = (1, 2, 3, 4, 5, 6, 7)

maxx = my_tuple[0]
minn = my_tuple[0]

for i in range(1, len(my_tuple)):

    if my_tuple[i] <= minn:
        minn = my_tuple[i]

    if my_tuple[i] >= maxx:
        maxx = my_tuple[i]

print("Maximum element in tuple :", maxx)
print("Minimum element in tuple :", minn)