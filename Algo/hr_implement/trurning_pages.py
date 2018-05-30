"""Given n and p , find and print the minimum number of pages Brie must turn in order to arrive at page p .
for n = 6 and p = 2 the minimum will be 1 turn to reach page p=2.
"""

def pageCount(n, p):
	#each turn has maximum of 2 pages; so,we are dividing it by 2
	#from front side it will be p divided by 2
	#from back side it will substraction of n divided by 2 and p divided by 2
	return int(min(p//2,n//2-p//2))

if __name__ == "__main__":
	print pageCount(6,2)


