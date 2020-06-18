
arr = [2,2,2,3,3,1,2,3,5,4,3,9,0,2]
mydict = {}

for i in arr:
    if(i in mydict):
        mydict[i] = mydict[i] + 1
    else:
        mydict[i] = 1

for key in mydict:
    if(mydict[key] == 1):
        print("Answer:", key)
        break