arr = [1,1,2,3,4]
arr1 = [1,1,1,1,1,2,2,2,2,2,2,3,5,4]
qTic = {}
val = 0
for i in arr1:
    if i in qTic:
        qTic[i] = qTic[i] + 1   
        val = i    
    else:
        if(len(qTic) > 0):
            print('i',i)
            #qTic.pop(val)
        qTic[i] = 1
        val = i  
print('qTic',qTic, val)
for x in qTic:
    print(x, qTic[x], 'fdf')
