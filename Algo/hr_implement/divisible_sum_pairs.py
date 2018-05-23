"""
You are given an array of  integers,N , and a positive integer, a0,a1....aN.
Find and print the number of  (i,j) pairs where i<j  and  ai+ aj is divisible by k .
"""
def divisibleSumPairs(n, k, ar):
	pairs = 0
	for i in range(n):
		for j in range(i+1,n):
			if (i < j) and ((ar[i]+ar[j]) % k == 0):
				pairs +=1
			
	print pairs

if __name__ == "__main__":
	n = 6
	k = 3
	ar = [1, 3 ,2, 6 ,1 ,2]
	divisibleSumPairs(n, k, ar)

