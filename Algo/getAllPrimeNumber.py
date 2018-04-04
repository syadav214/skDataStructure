#Given a number N, N>=2. Print all prime numbers <= N.

def CheckPrime(num):
    IsItPrime = True
    for i in range(2,num):
        if num%i == 0:
            IsItPrime = False
            break
    
    return IsItPrime          
        
def GetPrimeNumbers(N):
    arrayOfPrime = []
    i = 2
    while i <= N:
        if CheckPrime(i) == True:
            arrayOfPrime.append(i)
        i +=1        
    return arrayOfPrime

if __name__ == "__main__":
    N = int(raw_input().strip())
    print GetPrimeNumbers(N)