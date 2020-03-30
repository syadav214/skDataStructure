fibDict = {}
def fib(n):
    if(n in fibDict):
        return fibDict[n]
    #val = 0
    if(n==0):
        val = 0
    elif(n==1):
        val = 1
    elif(n==2):
        val = 1
    else:
        val = fib(n-1) + fib(n-2)
    
    fibDict[n] = val
    return val

for i in range(10):
    print(fib(i))