arr = [1,3,4,5,7,7,7,7,8,8,9,20]


def count(val,arr):
   index = find(val,arr)
   if index == None:
       return 0
   count = 1
   for i in range(index+1,len(arr)):
        if(arr[i] != val):
           return count
        count = count+1

def find(val,arr):
    half  = len(arr)//2
    if arr[0] > val or arr[len(arr)-1] < val:
        return None
    if arr[half] == val and arr[half-1] != val:
        return half
    if val > arr[half]:
        return half + 1 + find(val,arr[half+1:])
    if val <= arr[half]:
        return find(val,arr[:half])
    return None
print(count(8,arr))


