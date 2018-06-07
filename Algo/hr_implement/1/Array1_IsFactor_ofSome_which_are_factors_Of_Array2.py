"""
You will be given two arrays of integers. You will be asked to determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
"""

from functools import reduce


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def lcm_list(lst: list) -> int:
    return reduce(lcm, lst)


def gcd(a: int, b: int) -> int:
    while a % b != 0:
        a, b = b, (a % b)
    return b


def gcd_list(lst: list) -> int:
    return reduce(gcd, lst)

def getGCD(numbers):
	firstFactors = []
	finalFactors = []
	for i in range(len(numbers)):
		for j in range(2,numbers[i]+2):
			if numbers[i] % j == 0:
				if i == 0:
					firstFactors.append(j)
				elif i == 1 and j in firstFactors:
					finalFactors.append(j)	
	return max(finalFactors)
	
def getLCM(numbers):
	max_num = max(numbers)
	lcm =0
	while True:
		lcmChecker = []
		for i in range(len(numbers)):
			if max_num % numbers[i] == 0:
				lcmChecker.append(1)
			else:
				lcmChecker.append(0)
		
		if 0 in lcmChecker:
			max_num +=1
		else:
			lcm = max_num
			break
	return lcm

def getTotalX(a, b):
	lcm_value = getLCM(a)
	gcd_value = getGCD(b)
	counter = 0
	multiple_of_lcm = lcm_value
	while multiple_of_lcm <= gcd_value:
		if gcd_value % multiple_of_lcm ==0:
			counter += 1
		
		multiple_of_lcm += lcm_value
	
	print(counter)

if __name__ =="__main__":
	a = [2,4]
	b = [16,32,96]
	getTotalX(a,b)