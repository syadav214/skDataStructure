def solve(n, s, d, m):
	count = 0
	for i in range(n):
		print i, m+i, s[i:m+i]
		total = sum(s[i:m+i])
		if total == d:
			count +=1	
	return count

if __name__ == "__main__":
	n = 5
	s = [1, 2, 1, 3, 2]
	d = 3
	m = 2
	print solve(n,s,d,m)