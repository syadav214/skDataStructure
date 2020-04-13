arr = [-3,-1, 0, 1, 2, 6, 7, 9,10]
ranges = []
i = 0
while i < len(arr):
    start = arr[i]
    while(i+1 < len(arr) and arr[i] + 1 == arr[i+1]):
        i += 1
    end = arr[i]
    if(start != end):
        ranges.append(str(start)+'->'+str(end))
    else:
        ranges.append(str(start))
    i += 1

print(ranges)