def selection_sort(arr):
    for i in range(len(arr)):
        minimum_index = i
        for j in range(i,len(arr)):
            if arr[j] < arr[minimum_index]:
                minimum_index = j
        arr[i],arr[minimum_index] = arr[minimum_index],arr[i]
    return arr



if __name__ == "__main__":
    print(selection_sort([1,3,5,0,343,2]))  