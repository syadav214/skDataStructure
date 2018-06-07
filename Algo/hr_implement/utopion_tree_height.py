"""
Each spring, it doubles in height. Each summer, its height increases by 1 meter.
"""

def utopianTree(n):
	height =  1
	if n > 0:
		for i in range(1,n+1):
			if i%2 == 0:
				height +=1
			else:
				height *=2
	return height

if __name__ == "__main__":
	print utopianTree(0)
	print utopianTree(1)
	print utopianTree(4)