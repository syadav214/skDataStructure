"""
Print a flag if there are students available for given criteria.
"""

def angryProfessor(k, a):
	on_timers = 0
	for i in a:
		if i < 1:
			on_timers +=1
	if on_timers >= k:
		return 'NO'
	else:
		return 'YES'

if __name__ == "__main__":
	k = 2
	a = map(int,'0 -1 2 1'.split(' '))
	#a = map(int,'26 94 -95 34 67 -97 17 52 1 86'.split(' '))
	print angryProfessor(k,a)