"""
Append, Delete to match two strings in given moves
"""

def appendAndDelete(s, t, k):
	if (len(s)+ len(t)) < k:
		return 'Yes'

	i = 0
	for a in s:
		if i >= len(t) or a != t[i]:
			break
		i +=1

	diff = (len(s) - i) + (len(t) - i)
	print i, diff
	if (diff<=k and ((diff-k) % 2 ==0)):
		return 'Yes'
	else:
		return 'No'

if __name__ == "__main__":
	s = 'hackerhappy' 
	t = 'hackerrank'
	k = 9
	"""s = 'ashley'
	t = 'ash'
	k = 2"""
	"""s = 'aba'
	t = 'aba'
	k = 7"""
	print appendAndDelete(s,t,k)
