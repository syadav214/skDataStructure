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

"""
#arr = [3, 5, 7, 2]
#arr = [121, 23, 3, 333, 4]
#arr = [32, 42, 52, 62, 72, 82, 92]
arr =[1090, 1080, 1074, 1065, 1057, 1056, 1047, 1041, 1041, 1038, 1025, 1013, 1008, 992, 991, 991, 991, 978, 977, 959, 945, 935, 925, 925, 923, 915, 908, 904, 901, 901, 900, 897, 894, 882, 880, 876, 866, 854, 849, 849, 833, 818, 818, 812, 811, 809, 798, 794, 793, 788, 772, 763, 747, 746, 743, 737, 736, 734, 732, 730, 728, 718, 714, 713, 706, 701, 699, 691, 690, 689, 681, 672, 663, 656, 654, 653, 652, 651, 646, 644, 640, 637, 637, 635, 634, 633, 630, 625, 621]
arr = [1090, 1080, 1074, 1065, 1057, 1056, 1047, 1041, 1041, 1038, 1025, 1013, 1008, 992, 991, 991, 991, 978, 977, 959, 945, 935, 925, 925, 923, 915, 908, 904, 901, 901, 900, 897, 894, 882, 880, 876, 866, 854, 849, 849, 833, 818, 818,
       812, 811, 809, 798, 794, 793, 788, 772, 763, 747, 746, 743, 737, 736, 734, 732, 730, 728, 718, 714, 713, 706, 701, 699, 691, 690, 689, 681, 672, 663, 656, 654, 653, 652, 651, 646, 644, 640, 637, 637, 635, 634, 633, 630, 625, 621]


"""
