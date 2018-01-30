#Sparse Arrays

import sys

def printSparse(N,Nstring) :
    Q = int(raw_input().strip())
    for i in xrange(Q):
        Qsearch = raw_input().strip()
        count = 0
        for i in xrange(N):
            if Nstring[i] == Qsearch:
                count += 1
        print  count   

if __name__ == "__main__":
    N = int(raw_input().strip())
    Nstring = [[] for _ in xrange(N)]
    for i in xrange(N):
        Nstring[i] = raw_input().strip()
    printSparse(N,Nstring)
           


