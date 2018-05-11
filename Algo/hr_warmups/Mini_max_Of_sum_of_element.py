"""
Given five positive integers, find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""

def miniMaxSum(arr):
	min_num = min(arr)
	max_num = max(arr)
	sum_num = sum(arr)
	print((sum_num - max_num),(sum_num - min_num))
	

if __name__ == "__main__":
	arr = map(int, raw_input().rstrip().split())
	miniMaxSum(arr)