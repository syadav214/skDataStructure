"""
You have been asked to help study the population of birds migrating across the continent. 
Each type of bird you are interested in will be identified by an integer value. 
Each time a particular kind of bird is spotted, 
its id number will be added to your array of sightings. 
You would like to be able to find out which type of bird is most common given a list of sightings.
Your task is to print the type number of that bird and if two or more types of birds are equally common,
choose the type with the smallest ID number.
"""

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
	return max_occurance_type


if __name__ == "__main__":
	ar = [1, 4 ,4, 4 ,5, 3,3]
	migratoryBirds(ar)