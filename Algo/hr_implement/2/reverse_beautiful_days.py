"""
Given a range of numbered days [i..j], and a number k, determine the number of days in the range that are beautiful.
Beautiful numbers are defined as numbers where i - reverse(i) is evenly divisible by k. 
"""

def beautifulDays(i, j, k):
	count = 0 
	for x in range(i,j+1):
		reverse_number = int(''.join(reversed(str(x))))
		if (abs(x - reverse_number)) % k == 0:
			count +=1

	return count

if __name__ == "__main__":
	print beautifulDays(20,23,6)
