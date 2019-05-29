def checkDigits(numArr, chkNum):
    for num in numArr:
        # converts into an array like 123 will become str(num) = [1,2,3]
        # then check with given number
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
                        # get current array and append current num
                        newCombineArr.extend(cb)
                        newCombineArr.append(n)
                        combineArr.append(newCombineArr)
            else:
                # create combination
                combineArr.append([])
                combineArr.append([n])

        for cb in combineArr:
            if(len(cb) > 0):
                currSum = sum(cb)
                if(currSum > maxSum):
                    maxSum = currSum

        print(maxSum)


main()
