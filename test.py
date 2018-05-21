def breakingRecords(score):
	min_score = score[0]
	max_score = score[0]
	min_counter = 0
	max_counter = 0
	for i in range(1,len(score)):
		if min_score > score[i] :
			min_score = score[i]
			min_counter +=1
		if max_score < score[i]:
			max_score = score[i]
			max_counter +=1
	
	return [max_counter,min_counter]

if __name__ == "__main__":
	a = [3 ,4 ,21, 36, 10 ,28 ,35, 5, 24 ,42]
	a = [10, 5 ,20 ,20 ,4 ,5, 2, 25, 1]
	print breakingRecords(a)
