#!/bin/python
# maximum hourglass sum.

import sys


arr = []
sum = 0
maxLen = 5
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

for i in xrange(6):
    for j in xrange(6):
        tempSum = 0
        nextC2 = j + 1
        nextC3 = j + 2
        nextR2 = i + 1
        nextR3 = i + 2

        if nextC2 <= maxLen and nextC3 <= maxLen and nextR2 <= maxLen and  nextR3 <= maxLen:
                tempSum = arr[i][j] + arr[i][nextC2] + arr[i][nextC3] +  arr[nextR2][nextC2] + arr[nextR3][j] + arr[nextR3][nextC2] + arr[nextR3][nextC3]        
                #print(tempSum)
                if i == 0 and sum == 0:
                    sum = tempSum
                #print('1',sum)
                elif tempSum > sum:
                    sum = tempSum
                #print('2',sum)

print(sum)
