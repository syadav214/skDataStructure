def kangaroo(x1, v1, x2, v2):
	print x2-x1
	print v1-v2
	print (x2 - x1) % (v1-v2)
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