
#integer_on_Ticket = [0, -1, -2, 0, 0, 0]
integer_on_Ticket = [1, -1, 0, 7, 8, -5, 4]
#integer_on_Ticket = [-1, 7, 8, -5, 0, 4]
integer_on_Ticket = [-1, 7, 8, -5, 4]
#integer_on_Ticket = [3, 2, 1, -1]
#integer_on_Ticket = [11, 12, -2, -1]
#integer_on_Ticket = [3, 4, 5, 4]
#integer_on_Ticket = [4, 5, 4, 3]
integer_on_Ticket = [-1,-1,-1]
#integer_on_Ticket = [5, 10, 4, -1]
#integer_on_Ticket = [2,3,1,4,5]
N = len(integer_on_Ticket)

eleIndex = sorted(range(len(integer_on_Ticket)),key=lambda k: integer_on_Ticket[k], reverse=True)
new_integer_on_ticket = integer_on_Ticket[:]
new_integer_on_ticket.sort(reverse=True)

print(integer_on_Ticket, new_integer_on_ticket, eleIndex)

maxSum = 0
ticketPrint = []

for i in range(N):
    printArr = []
    blockIds = []
    currSum = 0
    currEle = new_integer_on_ticket[i]
    sortedIndex = eleIndex[i]
    blockIds.append(sortedIndex-1)        
    blockIds.append(sortedIndex+1)        
    # Backwards
    for b in range(sortedIndex - 1, -1, -1):
        bEle = integer_on_Ticket[b]
        if(b not in blockIds):
            printArr.insert(0,bEle)
            blockIds.append(b-1)
            blockIds.append(b+1)
            if(bEle>0):
                currSum += bEle


    printArr.append(currEle)
    if(currEle>0):
        currSum += currEle
    # Forwards
    for f in range(sortedIndex + 1, N):
        fEle = integer_on_Ticket[f]
        if(f not in blockIds):
            printArr.append(fEle)
            blockIds.append(f-1)
            blockIds.append(f+1)
            if(fEle>0):
                currSum += fEle
            
    if(printArr not in ticketPrint):  
        ticketPrint.append(printArr) 
        if(maxSum < currSum):
            maxSum = currSum            
        elif(maxSum == currSum):
            ticketArr = ticketPrint[0]
            prevLastEle = ticketArr[len(ticketArr)-1]
            currLastEle = printArr[len(printArr)-1]
            if(currLastEle > prevLastEle):
                ticketPrint.insert(0,printArr)        
    print('printArr',printArr)
        
print('ticketPrint',ticketPrint)
print('maxSum',maxSum)