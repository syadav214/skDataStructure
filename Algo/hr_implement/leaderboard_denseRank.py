"""
We want to determine Alice's rank as she progresses up the leaderboard in Dense Ranking.
"""

def climbingLeaderboard(scores, alice):
	x = set(scores)  
	x = list(x)      
	x.sort()          
	leng = len(x)+1
	lo = 0            
	result = []
	for score in alice:
		rank = leng   
		hi = leng - 1 
		while lo < hi:
			mid = (lo+hi)//2  
			if x[mid] <= score: lo = mid+1 
			else: hi = mid
		rank -= lo
		result.append(rank)

	return result 

def climbingLeaderboard2(scores, alice):
	scores = list(set(scores))
	result = []
	for i in alice:
		scores.append(i)
		#sorting is expensive here
		scores.sort(reverse = True)
		rank = scores.index(i)
		scores.remove(i)
		result.append(rank+1)
	return result


if __name__ == "__main__":
	scores = [100, 100, 50, 40, 40, 20, 10] 
	alice = [5, 25, 50, 120]
	print climbingLeaderboard(scores, alice)
