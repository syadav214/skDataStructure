
integer_on_Ticket = [-1, 7, 8, -5, 4]
# integer_on_Ticket = [3, 2, 1, -1]
# integer_on_Ticket = [11, 12, -2, -1]
#integer_on_Ticket = [3, 4, 5, 4]  #
# integer_on_Ticket = [4, 5, 4, 3]
# integer_on_Ticket = [5, 10, 4, -1]

N = 5
N = 4

sumIncluingPrevElement = 0
sumExcluingPrevElement = 0
elementArr = []
ticketNo = ''

for currElement in integer_on_Ticket:
    new_excl = max(sumIncluingPrevElement, sumExcluingPrevElement)
    sumIncluingPrevElement = sumExcluingPrevElement + currElement
    # print(sumExcluingPrevElement, currElement)
    elementArr.append([sumExcluingPrevElement, currElement])
    sumExcluingPrevElement = new_excl

maxSum = max(sumIncluingPrevElement, sumExcluingPrevElement)
print(maxSum)

for ele in elementArr:
    if(ele[0]+ele[1] == maxSum):
        if(ele[0] == 0):
              ticketNo = str(ele[1])
        else:
               ticketNo = str(ele[1]) + str(ele[0])
            break
