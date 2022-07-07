# 3) Python program to check if the list contains three conjugative numbers.

arr = [2,1,1,1,2,2,2,3]
l=len(arr)
for i in range(l-2):
	if arr[i] == arr[i+1] and arr[i+1] == arr[i + 2]:
		print(arr[i])









