"""Leap year before 1918 in Russia (Julian calender) was determine by divisble by 4
	After 1918 i.e. Gregorian calender => leap years determine with Divisible by 400 OR
	Divisible by 4 and not divisible by 100.
"""

def bonAppetite(n,k,bill,b):
	exp= (sum(bill[:k]) + sum(bill[k+1:]))/2
	if exp == b:
		print('Bon Appetit')
	else:
		print(int(b-exp)) # int used to get value without decimal


if __name__ == "__main__":
	nk_array = list(map(int,raw_input().strip().split(' ')))
	bill = list(map(int,raw_input().strip().split(' ')))
	b = int(raw_input().strip())
	bonAppetite(nk_array[0],nk_array[1],bill,b)

