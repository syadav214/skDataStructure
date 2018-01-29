#Dynamic Array   
rawData = map(int,raw_input().strip().split(' '))
N = rawData[0]
I = rawData[1]
lastAnswer = 0
seqList = [[] for _ in range(N)]

for i in xrange(I):
    rawData2 = map(int,raw_input().strip().split(' '))
    Q = rawData2[0]
    x = rawData2[1]
    y = rawData2[2]
    index = (x ^ lastAnswer) % N
    seq = seqList[index]
   
    if Q == 1:
        seq.append(y)
    elif Q == 2:
        size = len(seq)
        lastAnswer = seq[y%size]
        print lastAnswer
    #print seq , seqList
    

