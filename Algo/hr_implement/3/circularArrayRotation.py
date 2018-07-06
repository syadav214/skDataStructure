"""
For each array, perform a number of right circular rotations and return the value of the element at a given index.
"""

def circularArrayRotation(a, k, queries):
	array_a_len = len(a)	
	result = []
	
	for q in range(len(queries)):
		#subtract current query to rotation and take remainder from array's length
		index = (queries[q]- k) % array_a_len
		print (queries[q]- k), index
		result.append(a[index])
	
	return result

if __name__ == "__main__":
	a = [1, 2, 3]
	k = 2
	queries = [0,1,2]
	print circularArrayRotation(a, k, queries)