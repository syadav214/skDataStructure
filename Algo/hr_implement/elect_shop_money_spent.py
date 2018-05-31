elect_shop_money_spent.py

"""
Monica wants to buy a keyboard and a USB drive from her favorite electronics store. 
The store has several models of each. 
Monica wants to spend as much as possible for the  items, given her budget.
Print a single integer denoting the amount of money Monica will spend. 
If she doesn't have enough money to buy one keyboard and one USB drive, print -1 instead.
"""

def getMoneySpent(keyboards, drives, b):
	totalSpent=-1
	for x in keyboards:
		for y in drives:
			if x+y<=b:
				totalSpent=max(totalSpent,x+y)
	
	return(totalSpent)

if __name__ == "__main__":
	keyboards =[3, 1]
	drives = [5, 2, 8]
	b = 10
	#keyboards =[4]
	#drives = [4]
	#b = 5
	print getMoneySpent(keyboards,drives,b)