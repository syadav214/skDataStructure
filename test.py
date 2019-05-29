phases = [3, 0, 0]
states = [3, 0, 0]
phases = [3, 2, 1]
states = [1, 2, 2]
phases = [0, 1, 2, 2]
states = [2, 3]
phases = [2, 1, 0]
states = [1, 2]

maxInPhases = max(phases)
totInPhases = sum(phases)
possibleWinInPhase = 0
for i in phases:
    if(i > 0):
        possibleWinInPhase += 1


maxInStates = max(states)
totInStates = sum(states)
possibleWinInState = 0
for j in states:
    if(j > 0):
        possibleWinInState += 1

if(totInPhases == totInStates and possibleWinInPhase >= maxInStates and possibleWinInState >= maxInPhases):
    print('YES')
else:
    print('NO')
