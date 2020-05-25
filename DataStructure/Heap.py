class MaxHeap:

    def __init__(self,container):
        self.container = container


    def heapify(self,i):
        large = i 

        left = (2*i+1)
        if left < len(self.container) and self.container[left] >  self.container[large]:
            large = left

        right = 2*i +2 
        if right < len(self.container) and self.container[right] > self.container[large]:
            large = right

        if large != i:
            self.container[i] , self.container[large] = self.container[large],self.container[i]
            self.heapify(large)


    def build_heap(self):
        
        for i in range(len(self.container) // 2 , -1 , -1):
            self.heapify(i)

    def get_max(self):
        if self.container:
            maxNum = self.container[0]
            self.container[0] = self.container[len(self.container) - 1]
            self.container.pop()
            self.heapify(0)
            return maxNum


    def add(self,value):
        i = len(self.container)
        self.container.append(value)
        parent = (i-1) // 2
        while parent >= 0 and  value > self.container[parent]:
            self.container[i] , self.container[parent] = self.container[parent],self.container[i]
            i = parent 
            parent = (i-1) // 2


if __name__ == "__main__":
    nums  = [1,4,343,4,2,6,33,434]
    count = len(nums)
    print('Original array:')
    print(nums)
    heap = MaxHeap(nums)
    heap.build_heap()
    print('After construction Heap')
    print(nums)
    
    for i in range(3):
        print('Max:'),
        print(heap.get_max())
    

    heap.add(3333)
    print('Max:'),
    print(heap.get_max())

    print('Max:'),
    print(heap.get_max())