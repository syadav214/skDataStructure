"""
You are given queries in the form of x, y, z and representing the respective positions for cats A and B  and X for mouse . 
Complete the function to return the appropriate answer to each query, which will be printed on a new line.
"""

def catAndMouse(x, y, z):
	diff_x_z = abs(x - z )
	diff_y_z = abs(y - z)

	if diff_x_z == diff_y_z:
		return 'Mouse C'
	elif diff_x_z < diff_y_z:
		return 'Cat A'
	else:
		return 'Cat B'


if __name__ == "__main__":
	print catAndMouse(1,2,3)