"""
Division and cumulative likes on adverstisement. 
"""

def viralAdvertising(n):
	ads = 5
	refer = 3
	like_count = 0
	for i in range(1,n+1):
		tmp_like = abs(ads/2)
		like_count += tmp_like
		ads = tmp_like * refer		
	return like_count

if __name__ == "__main__":
	print viralAdvertising(4)
