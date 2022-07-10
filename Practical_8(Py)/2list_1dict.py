#P-8 Q.3 Python program to Convert two lists into a dictionary

L_Key = [1, 2, 3, 4]
L_Values=["One", "Two", "Three", "Four"]

print("Keys list :",L_Key)
print("Values list :",L_Values)

print("Dictionary of Keys & Values :",dict(zip(L_Key,L_Values)))