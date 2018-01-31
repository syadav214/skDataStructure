#Manipulate 

import sys




if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    nArray = [0] * (n+1)
    
    for a0 in xrange(m):
        a, b, k = raw_input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        nArray[a-1] += k
        if b <= len(nArray) :
            nArray[b] -= k;

    max = temp = 0
    for i in nArray:
        temp = temp + i
        if temp > max:
            max = temp
print max

