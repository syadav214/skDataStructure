def CreateStair(spaceCount,starCount):
	stair =""
	for i in range(spaceCount):
		stair = stair + " "
	for i in range(starCount):
		stair = stair + "*"
	return stair

if __name__ == "__main__":
	n = int(raw_input().strip())
	for i in range(1,n+1):
		print CreateStair(n-i,i)

