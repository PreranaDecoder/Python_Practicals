# P8 Q.1(b) Sort dictionary by Values.

dict = {1: 8, 2: 9, 3: 4}
sorted_dict = {}
sorted_keys = sorted(dict, key=dict.get)  # 1, 3, 2

for i in sorted_keys:
    sorted_dict[i] = dict[i]

print(sorted_dict)




