''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def getTicketNo(N,integer_on_Ticket):
    eleIndex = sorted(range(len(integer_on_Ticket)),
                      key=lambda k: integer_on_Ticket[k], reverse=True)
    new_integer_on_ticket = integer_on_Ticket[:]
    new_integer_on_ticket.sort(reverse=True)

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


def main():

    T = int(input())
    for i in range(T):
        N = int(input())
        integer_on_Ticket = list(map(int, input().split()))
        getTicketNo(N,integer_on_Ticket)


main()

