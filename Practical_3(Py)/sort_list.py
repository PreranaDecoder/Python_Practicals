# 5) Sort elements in ascending order and descending order.

arr = [3, 5, 6, 7, 1, 9, 5, 4, 3, 2]


# Ascending order -
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print("Ascending order -",arr)



# Descending order -
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print("Descending order -",arr)
