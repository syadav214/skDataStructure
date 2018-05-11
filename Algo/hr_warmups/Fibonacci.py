m = {}

def fib2(n):	
	f = 0
	for _k in range(n+1):
		if _k <= 2:
			f = 1
		else:
			f = m[_k-1] + m[_k-2]	
		m[_k] = f
	return m[n]

def fib(n):	
	f = 0
	if n in m:
		f = m[n]
	else:
		if n <= 2:
			f = 1
		else:
			f = fib(n-1) + fib(n-2)
		m[n] = f
	return f

if __name__ == "__main__":
	print fib2(7)