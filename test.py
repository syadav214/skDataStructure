"""
For each array, perform a number of right circular rotations and return the value of the element at a given index.
"""

def permutationEquation(p):
	result = []
	for i in range(len(p)):
		x = i + 1
		first_index = p.index(x)
		x = p.index(first_index + 1)
		result.append(x+1)	
	return result

if __name__ == "__main__":
	p = [2,3,1]
	p = [5,2,1,3,4]
	print permutationEquation(p)