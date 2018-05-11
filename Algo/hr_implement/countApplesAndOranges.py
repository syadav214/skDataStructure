""" 
 Given the value of  for  apples and  oranges, can you determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )? Print the number of apples that fall on Sam's house as your first line of output, then print the number of oranges that fall on Sam's house as your second line of output.
 """
 def countApplesAndOranges(s, t, a, b, apples, oranges):
		app_count=0
	oran_count=0
	for i in apples:
		apples_dis = a + i
		if apples_dis >= s and apples_dis <=t:
			app_count +=1
	
	for i in oranges:
		oranges_dis = b + i
		if oranges_dis >= s and oranges_dis <=t:
			oran_count +=1
	
	print app_count,oran_count
	

if __name__ == "__main__":
	s = 7
	t = 11
	a = 5
	b = 15
	apples= [-2,2,1]
	oranges = [5,-6]
	print countApplesAndOranges(s, t, a, b, apples, oranges)