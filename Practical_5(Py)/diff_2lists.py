from collections import Counter
# 5) Python program to compute the difference between two lists.
list1 = [1,2,3,4,5,6]
list2 = [2,3,4,5,7,8]

A=Counter(list1)
B=Counter(list2)
print(list(A-B))
print(list(B-A))