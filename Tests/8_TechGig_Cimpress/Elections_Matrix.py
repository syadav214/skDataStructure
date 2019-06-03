def main():
    T = int(input())

    for i in range(T):
        rc = input()
        phases = list(map(int, input().split()))
        states = list(map(int, input().split()))

        
        totInPhases = sum(phases)
        totInStates = sum(states)

        if(T==2):
            c = len(states)
            matrixScore = []

            for ri in phases:
                matrixScore.append(float(ri)/c)

            finalScore = sum(matrixScore)*c

            if(finalScore == totInStates):
                print("YES")
            else:
                print("NO")
        else:
            maxInPhases = max(phases)
            possibleWinInPhase = 0
            for i in phases:
                if(i > 0):
                    possibleWinInPhase += 1
            
            maxInStates = max(states)
            possibleWinInState = 0
            for j in states:
                if(j > 0):
                    possibleWinInState += 1

            if(totInPhases == totInStates and possibleWinInPhase >= maxInStates and  possibleWinInState >= maxInPhases):
                print('YES')
            else:
                print('NO')


main()
