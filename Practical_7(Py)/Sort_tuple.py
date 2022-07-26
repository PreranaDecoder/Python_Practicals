#P7 Q.5 Sort tuple by total digits.

def count_tuple_digits(row):
	return sum([len(str(element)) for element in row])

tuple = [(1, 2, 3, 4), (9, 8), (567,), (143, 234, 314)]
print("The tuple is :",tuple)

tuple.sort(key = count_tuple_digits)
print("The result is :",tuple)
