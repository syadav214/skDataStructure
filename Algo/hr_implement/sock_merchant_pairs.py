"""John works at a clothing store. He has a large pile of socks that he must pair them by color for sale.
You will be given an array of integers representing the color of each sock. 
Determine how many pairs of socks with matching colors there are
"""

def sockMerchant(n, ar):
	pair_hash = {}
	count = 0
	for i in range(n):
		if ar[i] in pair_hash:
			count +=1
			del pair_hash[ar[i]]
		else:
			pair_hash[ar[i]] = 1
	
	print count, pair_hash


if __name__ == "__main__":
	n = 9
	ar = [10 ,20, 20, 10, 10, 30, 50, 10, 20]
	sockMerchant(n,ar)

