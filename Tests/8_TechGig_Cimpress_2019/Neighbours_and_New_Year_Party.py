def main():
    T = int(input())
    integer_on_ticket = [0 for i in range(T)]

    for i in range(T):
        N = int(input())
        integer_on_ticket[i] = list(map(int, input().split()))

    for i in range(T):
        printMap = []

        def getMaxSum(arr):
            incl = 0
            excl = 0
            for i in arr:
                if excl > incl:
                    new_excl = excl
                else:
                    new_excl = incl
                incl = excl + i
                excl = new_excl
                printMap.append([incl, excl])
            return (excl if excl > incl else incl)

        arr = integer_on_ticket[i]
        totalSum = getMaxSum(arr)

        printDict = {}
        for printIndex in reversed(range(0, len(printMap))):
            if printMap[printIndex][0] > printMap[printIndex][1]:
                printDict[printMap[printIndex][0]] = printIndex
            else:
                printDict[printMap[printIndex][1]] = printIndex

        finalArr = []
        while totalSum > 0:
            printIndex = printDict[totalSum]
            totalSum = totalSum - arr[printIndex]
            finalArr.append(arr[printIndex])
        print(''.join(map(str, finalArr)))


main()

"""
#arr = [0, -1, -2, 0, 0, 0]
#arr = [1, -1, 0, 7, 8, -5, 4]
#arr = [-1, 7, 8, -5, 0, 4]
#arr = [-1, 7, 8, -5, 4]
#arr = [3, 2, 1, -1]
#arr = [11, 12, -2, -1]
#arr = [3, 4, 5, 4]
arr = [4, 5, 4, 3]
#arr = [0,0,0]
#arr = [5, 10, 4, -1]
#arr = [2,3,1,4,5]
"""
