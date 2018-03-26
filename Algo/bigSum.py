#find sum of big integers of an array

def aVeryBigSum(n, ar): 
    i = 0
    half = n/2
    oddArrayLen = False if n%2 == 0 else True
    sum = 0

    for x in xrange(half):
        sum = sum + ar[x] + ar[n-1-x]
        if oddArrayLen == True and half == x + 1:
            sum = sum + ar[half]            
    
    return sum


if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split(' '))
    print aVeryBigSum(n,arr)
