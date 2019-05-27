def main():
    T = int(input())

    for i in range(T):
        N = int(input())
        arr = list(map(int, input().split()))

        mainSet = set()

        def checkUniqueDigits(wholeNumber):
            isValid = True
            currSet = set(str(wholeNumber))
            if(currSet & mainSet):
                isValid = False
            mainSet.update(currSet)
            return isValid

        maxSum = 0
        arr.sort(reverse=True)

        for i in range(len(arr)):
            if i == 0:
                checkUniqueDigits(arr[i])
                maxSum = arr[i]
            else:
                if(checkUniqueDigits(arr[i])):
                    maxSum += arr[i]

        print(maxSum)


main()
