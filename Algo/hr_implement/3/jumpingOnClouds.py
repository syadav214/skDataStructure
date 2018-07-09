"""
give c= [0,0,1,0] and k =2 , the indices of her path are jumping with 2 jumps. 
Her energy level reduces by 1 for each jump and you landed on one thunderhead at an additional cost of 2 energy units.
Get final energy level.
"""

def jumpingOnClouds(c, k):
	E = 100
	for i in range(0,len(c),k):
		subVal = 1
		if c[i] == 1:
			subVal += 2
		E = E - subVal	
	return E

if __name__ == "__main__":
	c = map(int,('0 0 1 0 0 1 1 0'.split(' ')))
	k = 2
	print jumpingOnClouds(c,k)