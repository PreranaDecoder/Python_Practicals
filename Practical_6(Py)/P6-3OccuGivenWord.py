# P-6 Q-3) Program to print Occurrence of Given word in a string or sentence.

sentence = "My name is Prerana. My surname is Bhandari"
word = "My"
words = sentence.split()
count = 0
for i in words:
    if i == word:
        count += 1
print("Occurence of {0} in given sentence is {1}".format(word,str(count)))
