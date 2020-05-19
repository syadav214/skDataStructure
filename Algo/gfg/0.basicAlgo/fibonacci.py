def fib(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

fibDict = {}
def fibWithDict(n):
    if(n in fibDict):
        return fibDict[n]
    value = 0
    if(n==0):
        value = 0
    elif(n==1 or n==2):
        value = 1
    else:
        value = fib(n-1) + fib(n-2)
    
    fibDict[n] = value
    return value

print("Enter 'D' for dictionary and 'Any key' for simple recurison:")
ch = input()

for i in range(10):
    if(ch.upper() == 'D'):
        print(fibWithDict(i))
    else:
        print(fib(i))

