
def getResult(N, strength, energy):
    result = "WIN"
    for i in range(N):
        if (strength[i] > energy[i]):
            result = "LOSE"
            break
    
    return result

def main():

    T = int(input())
    for i in range(T):
        N = int(input())
        strength = list(map(int, input().split()))
        energy = list(map(int, input().split()))
        strength.sort()
        energy.sort()
        print(getResult(N, strength, energy))

main()

