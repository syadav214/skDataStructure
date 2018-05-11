B = [1, 2, 7, 9]
B = [1, 2, 4, 4]
sum = 8

hashTable = []
matched = False
for i in range(len(B)):
	comp = sum - B[i]
	if comp in hashTable:
		matched = True
		break

	hashTable.append(comp)
	print comp, B[i], matched

print 'matched=',matched

