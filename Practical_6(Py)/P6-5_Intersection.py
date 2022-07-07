# P-6 Q-5) Program to print Intersection of list.

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]
intersection = []
for i in list1:
    if i in list2:
        intersection.append(i)
print("Intersection of list :",intersection)
