"""
Calculate libraryFine
"""

def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    if y1>y2:
        fine = 10000
    elif y1<=y2:
        if m1>m2 and (y1>=y2):
            fine = 500 * (m1-m2)
        elif m1<=m2:
            if (d1>d2 and (m1-m2>=0) and (y1>=y2)):
                fine = 15*(d1-d2)
            else:
                fine = 0
    return fine



if __name__ =="__main__":
	d1 = 9
	m1 = 6
	y1 = 2015
	d2 = 6
	m2 = 6
	y2 = 2015
	print libraryFine(d1, m1, y1, d2, m2, y2)
