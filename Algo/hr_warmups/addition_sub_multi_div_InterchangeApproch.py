input1 = input().strip()

def solveProblem(input1):
	data = []
	opertorIndex = 0
	operator=""
	operatorFound = False
	i=0
	abc = ""
	for x in input1:	
		if x == "+" or x == "-" or x== "*" or x == "/":	
			temp =''.join(map(str,data[:i])) + x
			print temp
			data = []
			data.append(temp)
			"""if operatorFound == True:
				abc = Opertion(''.join(map(str,data[:opertorIndex])),''.join(map(str,data[opertorIndex:])),operator)
				print "abc",abc				
				data = []
				data.append(abc)
				abc = ""
				i = 1			
			operatorFound = True
			operator = x
			opertorIndex =  i	"""

		else: 
			data.append(x)
		i +=1
		#print data
	
	"""if operatorFound == True:
		print data[:opertorIndex],data[opertorIndex:]
		abc = Opertion(''.join(map(str,data[:opertorIndex])),''.join(map(str,data[opertorIndex:])),operator)"""
	
	return data

def Opertion(first,second,operator):
	if operator == "+":
		return first + second
	elif operator == "-":
		return second + first
	elif operator == "*":
		return first + second + "0"
	elif operator == "/":
		return second + "0" + first

print(solveProblem(input1))