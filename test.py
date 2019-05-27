mainSet = set()

def checkUniqueDigits(wholeNumber):
    print('wholeNumber',wholeNumber)
    isValid = True
    currSet = set(str(wholeNumber))
    print('currSet',currSet)
    if(currSet & mainSet):
        isValid = False
    mainSet.update(currSet)
    print('mainSet',mainSet)
    return isValid


#arr = [3, 5, 7, 2]
#arr = [121, 23, 3, 333, 4]
#arr = [32, 42, 52, 62, 72, 82, 92]
arr =[1090, 1080, 1074, 1065, 1057, 1056, 1047, 1041, 1041, 1038, 1025, 1013, 1008, 992, 991, 991, 991, 978, 977, 959, 945, 935, 925, 925, 923, 915, 908, 904, 901, 901, 900, 897, 894, 882, 880, 876, 866, 854, 849, 849, 833, 818, 818, 812, 811, 809, 798, 794, 793, 788, 772, 763, 747, 746, 743, 737, 736, 734, 732, 730, 728, 718, 714, 713, 706, 701, 699, 691, 690, 689, 681, 672, 663, 656, 654, 653, 652, 651, 646, 644, 640, 637, 637, 635, 634, 633, 630, 625, 621]

arr.sort(reverse=True)

for x in range(10):
    maxSum = 0    
    for i in range(len(arr)):
        if i == 0:
            checkUniqueDigits(arr[i])
            maxSum = arr[i]
        else:
            if(checkUniqueDigits(arr[i])):
                maxSum += arr[i]
    arr.pop(0)
    print(maxSum)
