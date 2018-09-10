def bubble(arr):
    for j in range(0,len(arr)):
        swap  = 0
        for i in range(0,len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
                swap +=1

        if swap == 0:
            break
    return arr


print(bubble([1,43,54,54,3,1,4,65,969,4,2,123]))

    
