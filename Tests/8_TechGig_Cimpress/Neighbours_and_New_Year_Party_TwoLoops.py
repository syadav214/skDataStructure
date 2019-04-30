''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def getTicketNo(N, integer_on_Ticket):
    maxSum = 0
    ticketNumber = 0
    prevMin = 0

    for i in range(N):
        for j in range(i+2, N):
            sumEle = integer_on_Ticket[i] + integer_on_Ticket[j]
            if(sumEle >= maxSum):
                if(sumEle == maxSum):
                    currPrevMin = min(integer_on_Ticket[i], integer_on_Ticket[j])
                    if(currPrevMin > prevMin):
                        ticketNumber = str(min(integer_on_Ticket[i], integer_on_Ticket[j])) + str(max(integer_on_Ticket[i], integer_on_Ticket[j]))
                else:
                    prevMin = min(integer_on_Ticket[i], integer_on_Ticket[j])
                    ticketNumber = str(min(integer_on_Ticket[i], integer_on_Ticket[j])) + str(max(integer_on_Ticket[i], integer_on_Ticket[j]))
                maxSum = sumEle
        
        if(integer_on_Ticket[i] > maxSum):
            ticketNumber = integer_on_Ticket[i]
            maxSum = integer_on_Ticket[i]
    
    return ticketNumber


def main():

    T = int(input())
    for i in range(T):
        N = int(input())
        integer_on_Ticket = list(map(int, input().split()))
        print(getTicketNo(N, integer_on_Ticket))

main()

