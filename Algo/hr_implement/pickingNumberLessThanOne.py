"""
Given an array of integers, find and print the maximum number of integers you can 
select from the array such that the absolute difference between any two of the chosen integers is less than or equal to 1 .
 For example, if your array is a = [1,1,2,2,4,4,5,5,5] and you can create two subarrays meeting the criterion: [1,1,2,2]and [4,4,5,5,5]. 
 The maximum length subarray has 5 elements.
"""

def pickingNumbers(a):
	maximum = 0
	for i in a:
		count_curr = a.count(i)
		count_curr_minus_one= a.count(i-1)
		sum_of_counts = count_curr + count_curr_minus_one
		if sum_of_counts  > maximum:
			maximum = sum_of_counts 
	
	return maximum


if __name__ == "__main__":
	a = [4, 6, 5, 3, 3, 1]
	print pickingNumbers(a)
