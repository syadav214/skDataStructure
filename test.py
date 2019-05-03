
#integer_on_Ticket = [0, -1, -2, 0, 0, 0]
integer_on_Ticket = [-1, 7, 8, -5, 4]
integer_on_Ticket = [3, 2, 1, -1]
integer_on_Ticket = [11, 12, -2, -1]
integer_on_Ticket = [3, 4, 5, 4]
#integer_on_Ticket = [4, 5, 4, 3]
#integer_on_Ticket = [5, 10, 4, -1]
#integer_on_Ticket = [2,3,1,4,5]
N = len(integer_on_Ticket)

eleIndex = sorted(range(len(integer_on_Ticket)),
                  key=lambda k: integer_on_Ticket[k], reverse=True)
new_integer_on_ticket = integer_on_Ticket[:]
new_integer_on_ticket.sort(reverse=True)


print(integer_on_Ticket, new_integer_on_ticket, eleIndex)

maxVal = 0
minVal = 0
printingTicketVal = []
x = N if(N < 100) else 1
for mainIndex in range(x):
    prevVal = new_integer_on_ticket[mainIndex]
    printingTicketIndex = []
    currVal = 0
    if(prevVal > 0):
        prevIndex = eleIndex[mainIndex]
        evenOrOdd = prevIndex % 2 == 0        
        printingTicketIndex.append(prevIndex)        
        currVal += prevVal
        adjIds = []
        adjIds.append(prevIndex+1)
        adjIds.append(prevIndex-1)
        for i in range(N):
            if (integer_on_Ticket[i] == 0):
                continue

            if(i == 0 and evenOrOdd == False):
                continue

            if (prevIndex != i and integer_on_Ticket[i] > 0 and i not in adjIds):
                currVal += integer_on_Ticket[i]
                printingTicketIndex.append(i)
                adjIds.append(i+1)
                adjIds.append(i-1)
        if(currVal > maxVal):
            maxVal = currVal
            minVal = integer_on_Ticket[max(printingTicketIndex)]
            printingTicketVal = printingTicketIndex
        elif currVal == maxVal:
            maxOfMinVal = integer_on_Ticket[max(printingTicketIndex)]
            if(maxOfMinVal > minVal):
                minVal = maxOfMinVal
                printingTicketVal = printingTicketIndex

printingTicketVal.sort(reverse=True)
finalStr = ''
for currEle in printingTicketVal:
    finalStr += str(integer_on_Ticket[currEle])
print(finalStr)
