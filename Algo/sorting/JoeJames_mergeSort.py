arr = [4,6,7,8,35,5]

def merge(arr, first, middle, last):
    #print(arr, first, middle, last)
    L = arr[first:middle]
    R = arr[middle:last+1]
    print(L,R)
    L.append(1111111)
    R.append(1111111)

    i=j=0

    for k in range(first, last):
        if(L[i] <= R[j]):
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1

def mergeSort2(arr, first, last):
    if(first < last):
        middle = (first + last) // 2
        #print('middle',middle)
        mergeSort2(arr, first, middle)
        mergeSort2(arr, middle+1, last)
        merge(arr, first, middle, last)

def mergeSort(arr):
    mergeSort2(arr, 0, len(arr))
    print(arr)


mergeSort(arr)
