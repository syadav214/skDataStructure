def getTicketNo(integer_on_Ticket):    
    sumIncluingPrevElement = 0
    sumExcluingPrevElement = 0
    elementArr = []
    ticketNo = ''

    for currElement in integer_on_Ticket:
        new_excl = max(sumIncluingPrevElement, sumExcluingPrevElement)
        sumIncluingPrevElement = sumExcluingPrevElement + currElement
        elementArr.append([sumExcluingPrevElement, currElement])
        sumExcluingPrevElement = new_excl
    
    maxSum = max(sumIncluingPrevElement, sumExcluingPrevElement)
    for ele in elementArr:
        if(ele[0]+ele[1] == maxSum):
            if(ele[0] == 0):
                ticketNo = str(ele[1])
            else:
                ticketNo = str(ele[1]) + str(ele[0])
            break
    
    return ticketNo


def main():

    T = int(input())
    for i in range(T):
        N = int(input())
        integer_on_Ticket = list(map(int, input().split()))
        print(getTicketNo(integer_on_Ticket))

main()

