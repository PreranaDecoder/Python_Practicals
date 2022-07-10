# TELEPHONE DIRECTORY

# A) finding value-key:value
# B) replacing value-key: new value
# C) replacing key value - delete key and insert new key

def dash():
    for i in range(0, 70):
        print("-", end="")
    print("\n")


tel_dir = {"Prerana": 9876543210, "PAPA": 9876543211, "AAI": 9876543212, "KALYA": 9876543213,
           "DADA": 9876543214, "MAMA": 9876543215, "BHUSHAN": 9876543216, "PRAJOT": 9876543217,
           "RUTUJA": 9876543218, "MAYUR": 9876543219}
print("Telephone directory is : ")
print(tel_dir)


# A) finding value-key:value    
key = str(input("Enter key to find value : "))
print("Telephone number of given key " + key + " is : ")
for i in tel_dir.keys():
    if i == key:
        print(tel_dir[i])


dash()
# B) replacing value-key : new value
key = str(input("Enter key to replace value : "))
value = str(input("Enter new value : "))
for i in tel_dir.keys():
    if i == key:
        tel_dir[i] = value
print("Telephone directory after replacement : ")
print(tel_dir)


dash()
# C) Replacing key value - delete key and insert new key

num = int(input("Enter telephone number : "))
name = str(input("Enter new key name : "))
old_key = 0
for key, value in tel_dir.items():
    if num == value:
        old_key = key
tel_dir[name] = tel_dir.pop(key)

print("Dictionary after replacing key:value : ")
print(tel_dir)
