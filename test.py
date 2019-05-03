
integer_on_Ticket = [-1, 7, 8, -5, 4]
#integer_on_Ticket = [3, 2, 1, -1]
#integer_on_Ticket = [11, 12, -2, -1]
#integer_on_Ticket = [3, 4, 5, 4]#, 0, 1]
#integer_on_Ticket = [4, 5, 4, 3]
#integer_on_Ticket = [5, 10, 4, -1]
#integer_on_Ticket = [2,3,1,4,5]

N = 5
N = 4

eleIndex = sorted(range(len(integer_on_Ticket)),
                  key=lambda k: integer_on_Ticket[k], reverse=True)
new_integer_on_ticket = integer_on_Ticket[:]
new_integer_on_ticket.sort(reverse=True)

print(integer_on_Ticket, new_integer_on_ticket, eleIndex)

allTicket = []

for mainIndex in range(len(new_integer_on_ticket)):
    prevVal = new_integer_on_ticket[mainIndex]
    printingTicketIndex = []
    printingTicketVal = []
    if(prevVal > 0):
        prevIndex = eleIndex[mainIndex]
        evenOrOdd = prevIndex % 2 == 0
        printingTicketIndex.append(prevIndex)
        printingTicketVal.append(integer_on_Ticket[prevIndex])
        for i in range(mainIndex + 1, len(new_integer_on_ticket)):
            currIndex = eleIndex[i]
            if (evenOrOdd == (currIndex % 2 == 0) and new_integer_on_ticket[i] > 0):
                printingTicketIndex.append(currIndex)
                printingTicketVal.append(integer_on_Ticket[currIndex])
        allTicket.append([prevIndex, printingTicketIndex, printingTicketVal])


print('**************')
maxVal = 0
minVal = 0
printIndex = 0

for i in range(len(allTicket)):
    currSum = sum(allTicket[i][2])
    print('currSum', currSum, maxVal)
    if(currSum > maxVal):
        print('yes')
        maxVal = currSum
        printIndex = i
    elif(currSum == maxVal):
        print('no')
        maxOfMinVal = min(allTicket[i][2])
        if(maxOfMinVal > minVal):
            minVal = maxOfMinVal
            printIndex = i
        maxVal = currSum
    print(allTicket[i])

print('**************')
print(printIndex)

print('**************')
printingTicket = allTicket[printIndex][1]
printingTicket.sort(reverse=True)
finalStr = ''
for currEle in printingTicket:
    finalStr += str(integer_on_Ticket[currEle])
print(finalStr)

"""


for i in range(1, len(new_integer_on_ticket)):
    currIndex = eleIndex[i]
    if (evenOrOdd == (currIndex % 2 == 0) and new_integer_on_ticket[i] > 0):
        print(new_integer_on_ticket[i], currIndex)
        printingTicket.append(currIndex)

print('**************')
printingTicket.sort(reverse=True)
finalStr = ''
for currEle in printingTicket:
    finalStr += str(integer_on_Ticket[currEle])
print(finalStr)

"""
