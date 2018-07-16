"""
number of squares in a given range. We have formula to find out the same.
"""
import math

def squares(a, b):	
	return (int)((math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a))) + 1)

if __name__ == "__main__":
	print squares(17,24)