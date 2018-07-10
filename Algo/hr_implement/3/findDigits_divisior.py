"""
The number 12 is broken into two digits, 1 and 2 . When is divided by either of those two digits, the remainder is 0 so they are divisors.
"""

def findDigits(n):
	count = 0
	for i in str(n):
		if i !='0' and n%int(i)==0:
			count +=1
	
	return count

if __name__ == "__main__":
	print findDigits(1012)