#3) Print largest and smallest element in array.

arr = [1, 5, 4, 3, 7, 6, 8, 9]
minn = arr[0]
maxx = arr[0]
for i in range(len(arr)):
    if arr[i] < minn :
        minn = arr[i]
    if arr[i] > maxx :
        maxx = arr[i]
print("Smallest element in list -",minn)
print("Largest element in list -",maxx)
