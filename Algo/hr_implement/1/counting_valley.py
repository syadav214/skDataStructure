"""
The first line contains an integer n , the number of steps in Gary's hike. 
The second line contains a single string s, of n characters describing his path.
Print a single integer denoting the number of valleys Gary walked through during his hike.
If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:
_/\      _
   \    /
    \/\/
	He enters and leaves one valley.
"""
def countingValleys(n, s):
	curr_level = 0
	vally_counter = 0
	below_sea_level = False
	for i in range(n):
		if s[i] == "U":
			curr_level +=1
		else:
			curr_level -=1
		
		if below_sea_level == False:
			if curr_level < 0:
				below_sea_level = True
		elif curr_level==0:
			below_sea_level = False
			vally_counter +=1

	return vally_counter

if __name__ == "__main__":
	print countingValleys(10,'UDUUUDUDDD')