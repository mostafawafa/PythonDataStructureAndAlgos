from LinkedList import LinkedList 
from Node import Node

class Queue:

    def __init__(self):
        self.container = LinkedList()

    def enqueue(self,val):
        node = Node(val)
        self.container.addToEnd(node)
    
    def dequeue(self):
        return self.container.removeFromStart().val




if __name__ == "__main__":
    queue = Queue()
    print('enqueue 4')
    queue.enqueue(4)
    print('enqueue 5')
    queue.enqueue(5)
    print('dequeue from queue:')
    print(queue.dequeue())



