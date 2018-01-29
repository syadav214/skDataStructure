# Left Rotation of array

import sys

def leftRotation(a, d):
    finalArray = [[] for _ in range(lenArray)]
    for i in range(len(a)):
        index = i - d
        if index < 0:
            index = len(a) + index
        finalArray[index]= a[i]
    return finalArray
        

if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = map(int, raw_input().strip().split(' '))
    finalArray = leftRotation(a, d)
    print " ".join(map(str, finalArray))


