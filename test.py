
#integer_on_Ticket = [0, -1, -2, 0, 0, 0]
integer_on_Ticket = [1,-1, 7, 0, 8, -5, 4]
#integer_on_Ticket = [3, 2, 1, -1]
#integer_on_Ticket = [11, 12, -2, -1]
#integer_on_Ticket = [3, 4, 5, 4]
#integer_on_Ticket = [4, 5, 4, 3]
#integer_on_Ticket = [5, 10, 4, -1]
#integer_on_Ticket = [2,3,1,4,5]
N = len(integer_on_Ticket)

eleIndex = sorted(range(len(integer_on_Ticket)),
                  key=lambda k: integer_on_Ticket[k], reverse=True)
new_integer_on_ticket = integer_on_Ticket[:]
new_integer_on_ticket.sort(reverse=True)

maxSum = 0

for i in range(N):
    currEle = new_integer_on_ticket[i]
    if currEle > 0:
        currSum = currEle
        sortedIndex = eleIndex[i]
        # Backwards
        print('currEle', currEle)
        for b in range(sortedIndex - 1, -1, -1):
            bEle = integer_on_Ticket[b]
            if(bEle == 0):
                continue
            print('b', integer_on_Ticket[b])

        for f in range(sortedIndex + 1, N):
            fEle = integer_on_Ticket[f]
            if(fEle == 0):
                continue
            print('f', integer_on_Ticket[f])


print(integer_on_Ticket, new_integer_on_ticket, eleIndex)
