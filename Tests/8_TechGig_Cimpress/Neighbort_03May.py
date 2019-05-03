def getTicketNo(integer_on_Ticket):
    eleIndex = sorted(range(len(integer_on_Ticket)),
                      key=lambda k: integer_on_Ticket[k], reverse=True)
    new_integer_on_ticket = integer_on_Ticket[:]
    new_integer_on_ticket.sort(reverse=True)

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
            allTicket.append(
                [prevIndex, printingTicketIndex, printingTicketVal])

    maxVal = 0
    minVal = 0
    printIndex = 0

    for i in range(len(allTicket)):
        currSum = sum(allTicket[i][2])
        if(currSum > maxVal):
            maxVal = currSum
            printIndex = i
        elif(currSum == maxVal):
            maxOfMinVal = min(allTicket[i][2])
            if(maxOfMinVal > minVal):
                minVal = maxOfMinVal
                printIndex = i
            maxVal = currSum

    printingTicket = allTicket[printIndex][1]
    printingTicket.sort(reverse=True)
    finalStr = ''
    for currEle in printingTicket:
        finalStr += str(integer_on_Ticket[currEle])
    print(finalStr)


def main():

    T = int(input())
    for i in range(T):
        N = int(input())
        integer_on_Ticket = list(map(int, input().split()))
        getTicketNo(integer_on_Ticket)


main()
