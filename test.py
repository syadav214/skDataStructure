
#integer_on_Ticket = [0, -1, -2, 0, 0, 0]
#integer_on_Ticket = [1, -1, 0, 7, 8, -5, 4]
#integer_on_Ticket = [-1, 7, 8, -5, 0, 4]
integer_on_Ticket = [-1, 7, 8, -5, 4]
#integer_on_Ticket = [3, 2, 1, -1]
#integer_on_Ticket = [11, 12, -2, -1]
#integer_on_Ticket = [3, 4, 5, 4]
#integer_on_Ticket = [4, 5, 4, 3]
integer_on_Ticket = [5, 10, 4, -1]
integer_on_Ticket = [2,3,1,4,5]
N = len(integer_on_Ticket)

eleIndex = sorted(range(len(integer_on_Ticket)),key=lambda k: integer_on_Ticket[k], reverse=True)
new_integer_on_ticket = integer_on_Ticket[:]
new_integer_on_ticket.sort(reverse=True)

print(integer_on_Ticket, new_integer_on_ticket, eleIndex)

maxSum = 0
ticketPrint = []

for i in range(N):
    currEle = new_integer_on_ticket[i]
    if currEle > 0:
        printArr = []
        currSum = currEle
        sortedIndex = eleIndex[i]
        printArr.append(sortedIndex)
        validIndex = sortedIndex - 1
        # Backwards
        for b in range(sortedIndex - 1, -1, -1):
            bEle = integer_on_Ticket[b]
            if(bEle == 0):
                validIndex = validIndex - 1
                continue
            if(b == validIndex):
                continue
            validIndex = b - 1
            if(bEle > 0):
                currSum += bEle
                printArr.append(b)

        validIndex = sortedIndex + 1
        # Forwards
        for f in range(sortedIndex + 1, N):
            fEle = integer_on_Ticket[f]
            if(fEle == 0):
                validIndex = validIndex + 1
                continue
            if(f == validIndex):
                continue
            validIndex = f + 1
            if(fEle > 0):
                currSum += fEle
                printArr.append(f)

        if(currSum > maxSum):
            maxSum = currSum
            ticketPrint = printArr
        elif currSum == maxSum:
            maxLastEle = integer_on_Ticket[max(ticketPrint)]
            currMaxLastEle = integer_on_Ticket[max(printArr)]
            if(currMaxLastEle > maxLastEle):
                ticketPrint = printArr

ticketPrint.sort(reverse=True)
finalStr = ''
for currEle in ticketPrint:
    finalStr += str(integer_on_Ticket[currEle])
print(finalStr)
