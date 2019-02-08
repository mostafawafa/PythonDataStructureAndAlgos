

#
# TO GET THE number of times any value occur in sorted array
# You should add a number a args like this: python occurances.py 3

import sys

arr = [1,2,2,2,3,3,5,10,10]


def bfs(arr,element,l,h):

    mid = (l+h) // 2
    if arr[mid] == element:
        return  mid
    if(l >= h ) :
        return False
    if arr[mid] > element:
        return  bfs(arr,element,l,mid-1)
    if arr[mid] < element:
        return  bfs(arr,element,mid+1,h)


def occurences(arr,element):
    length = len(arr)
    index =  bfs(arr,element,0,length-1)
    if not index:
        return 0
    count = 1
    nextIndex = index + 1
    prevIndex = index - 1
    if (nextIndex == length or  nextIndex < 0):
            return count
    while(arr[nextIndex] == element  ):
        count +=1
        nextIndex += 1  
        if nextIndex == length:
            break
    while(arr[prevIndex] == element):
        count +=1
        prevIndex -= 1 
        if nextIndex < 0:
            break

    return count



print(occurences(arr,int(sys.argv[1])))