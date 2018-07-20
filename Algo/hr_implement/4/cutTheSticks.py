"""
get smallest number, remove the number from the array with subtracting each element with the smallest number and print length from the array.
Do the same till length is zero. 
"""

def cutTheSticks(arr):
    result = []
    len_arr = len(arr)
    result.append(len_arr)    
    while len_arr > 0:
        smallest = min(arr)
        newArr = []
        for i in range(len(arr)):
            if smallest != arr[i]:
                newArr.append(arr[i]-smallest)        
        arr = newArr
        len_arr = len(arr)
        if len_arr ==0:
            break

        result.append(len_arr)
    
    return result


if __name__ == "__main__":
    arr = [5, 4, 4, 2, 2, 8]
    arr = [1, 2, 3, 4, 3, 3, 2, 1]    
    print cutTheSticks(arr)
