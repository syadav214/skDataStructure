def checkDigits(numArr, chkNum):
    for num in numArr:
        for val in str(num):
            if val in str(chkNum):
                return True
                break
    return False


def main():
    T = int(input())

    for i in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        arr = list(set(arr))
        arr.sort(reverse=True)
        combineArr = []
        maxSum = 0
        for n in arr:
            if(len(combineArr) > 0):
                for cb in combineArr:
                    if(checkDigits(cb, n) == False):
                        newCombineArr = []
                        newCombineArr.extend(cb)
                        newCombineArr.append(n)
                        combineArr.append(newCombineArr)
            else:
                combineArr.append([])
                combineArr.append([n])

        for cb in combineArr:
            if(len(cb) > 0):
                currSum = sum(cb)
                if(currSum > maxSum):
                    maxSum = currSum

        print(maxSum)


main()
