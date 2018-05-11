"""
Complete the function kangaroo which takes starting location and speed of both kangaroos as input,
 and return  or  appropriately. 
 Can you determine if the kangaroos will ever land at the same location at the same time? 
 The two kangaroos must land at the same location after making the same number of jumps.
 """

def kangaroo(x1, v1, x2, v2):
	"""
	 If the % !== 0 then (x2-x1) the diference between both start points 
	 it's not divisible with (v2-v1) the diference of speed 
	 then they never will land on the same spot at the same time.
	  4%2 is 0 5%2 = 1 because 5/2 is 2*2 + 1
	"""
	if ((v1 > v2) and ((x2 - x1) % (v1-v2) ==0)):
		print 'YES'
	else:
		print 'NO'
	

if __name__ == "__main__":
	x1 =0
	v1 = 3
	x2 = 4
	v2 = 2
	kangaroo(x1, v1, x2, v2)