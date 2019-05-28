phases = [3, 0, 0]
states = [3, 0, 0]
phases = [3, 2, 1]
states = [1, 2, 2]
phases = [2, 1, 0]
states = [1, 2]


p = len(phases)
s = len(states)

phases.sort(reverse = True)
states.sort(reverse = True)

matrix = [['X']*s for i in range(p)]
matrix[0][0] = 1
print(matrix)


# if(sum(phases) == sum(states)):
