"""
Extra Long Factorials
"""

def extraLongFactorials2(n):
	if(n==1):
		return 1
	prod = n * extraLongFactorials2(n-1)
	return prod

def extraLongFactorials(n):
	x = n
	mutli = 1
	for i in range(1,n):
		mutli = mutli * x
		x = x - 1	
	return mutli

if __name__ == "__main__":
	print extraLongFactorials2(5)