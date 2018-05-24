def migratoryBirds(ar):
	max_val = max(ar)
	count_hash = {}	
	for i in range(len(ar)):
		if ar[i] in count_hash:
			prev_count = count_hash[ar[i]]
			count_hash[ar[i]] = prev_count + 1
		else:
			count_hash[ar[i]] = 1
	
	max_occurance_type = max(count_hash,key=count_hash.get)
	print max_occurance_type
	print count_hash[max_occurance_type]


if __name__ == "__main__":
	ar = [1, 4 ,4, 4 ,5, 3,3]
	migratoryBirds(ar)