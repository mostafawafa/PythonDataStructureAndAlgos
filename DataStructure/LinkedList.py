from Node import Node



class LinkedList:

    def __init__(self,val = []): 
        self.head = None
        self.tail = None
        if(isinstance(val, list)):
            self.convertList(val)


    def convertList(self,arr):
        for val in arr:
            node = Node(val)
            self.addToEnd(node)
            

    def addToStart(self,node):
        if(self.head == None):
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head = node


    def removeFromStart(self):
        node = self.head
        self.head = node.next
        return node

    def addToEnd(self,node):
        if(self.head == None):
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def traverse(self):
        node = self.head 
        while node != None:
            print(node.val)
            node = node.next 



if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.addToEnd(Node(5))
    linkedlist.addToEnd(Node(2))
    linkedlist.addToEnd(Node(54))
    linkedlist.addToStart(Node(1))

    linkedlist.traverse()