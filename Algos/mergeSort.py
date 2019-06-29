def mergeSort(arr):

    length = len(arr)
    if(length == 1):
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left =  mergeSort(left) 
    right = mergeSort(right)

    sortedArr = []
    leftLen = len(left)
    rightLen = len(right)
    i = j = 0

    while i < leftLen and j < rightLen : 
        if left[i] < right[j]:
            sortedArr.append( left[i])
            i +=1
        else:
            sortedArr.append( right[j])
            j +=1

    if(i < leftLen):
         while(i < leftLen):
            sortedArr.append( left[i])
            i +=1

    if(j < rightLen):
         while(j < rightLen):
            sortedArr.append( right[j])
            j +=1

    return sortedArr


if __name__ == "__main__":
    print(mergeSort([4,54,6,5,4]))

