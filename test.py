"""Leap year before 1918 in Russia (Julian calender) was determine by divisble by 4
	After 1918 i.e. Gregorian calender => leap years determine with Divisible by 400 OR
	Divisible by 4 and not divisible by 100."""
	
def solve(year):
	day_of_programmer = ''
	if year == 1918:
		day_of_programmer = '26.09.'
	elif ((year<1918) and (year%4==0)) or ((year%400==0) or ((year%4==0) and (year%100!=0))):
		day_of_programmer = '12.09.'
	else:
		day_of_programmer = '13.09.'
	
	return day_of_programmer + str(year)


if __name__ == "__main__":
	print solve(1800)