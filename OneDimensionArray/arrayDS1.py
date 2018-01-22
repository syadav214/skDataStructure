#reverse order of array
import sys


n = int(raw_input().strip())

arr = map(int,raw_input().strip().split(' '))

printedData = ''

for x in reversed(arr):
    printedData = printedData + str(x) + ' '

print(printedData)