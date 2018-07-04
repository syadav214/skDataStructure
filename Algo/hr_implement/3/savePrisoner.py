"""
There are prisoners 4 and 6 pieces of candy. The prisoners arrange themselves in seats numbered 1 to 4. 
Let's suppose two is drawn from the hat. Prisoners receive candy at positions 2,3,4,1,2,3. 
The prisoner to be warned sits in chair number 3.
"""

def saveThePrisoner2(n, m, s):
	for i in range(m):
		if i > s:
			i = i - s
		else:
			i = i + s	
	return i

def saveThePrisoner(nOfPrisoners, candies, startingPoint):
	a=0
	#subtract 1 from startingPoint as we taking position of prisoners as Array
	#Add candies and find remainder
	a=((startingPoint-1) + candies) % nOfPrisoners
	if a==0:
		return nOfPrisoners
	else:
		return a

if __name__ == "__main__":
	print saveThePrisoner(5,2,2)