# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
N = len(arr)
x = 0

for i in range(N):
    if(arr[i] == 'R'):
        arr[x], arr[i] = arr[i], arr[x]
        x += 1


for i in range(N):
    if(arr[i] == 'G'):
        arr[x], arr[i] = arr[i], arr[x]
        x += 1

print(arr)
