from LinkedList import LinkedList 
from Node import Node

class Stack:

    def __init__(self):
        self.container = LinkedList()

    def push(self,val):
        node = Node(val)
        self.container.addToStart(node)
    
    def pop(self):
        return self.container.removeFromStart().val





if __name__ == "__main__":
    stack = Stack()
    print('push 4')
    stack.push(4)
    print('push 5')
    stack.push(5)
    print('pop from stack:')
    print(stack.pop())


