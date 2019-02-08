from LinkedList import LinkedList



class Graph:

    def __init__(self): 
       self.vertices = {}
       self.visited = []

    
    def push(self,v,e):
        self.vertices[v] = LinkedList(e)


    def getNegibours(self,v):  
        return self.vertices[v]


    def dfsSearch(self,v,val):
        self.visited.append(v)
        return self.dfs(v,val)

    def dfs(self,v,val):
        neigbours =  self.getNegibours(v)
        node = neigbours.head
        if v == val:
            return True
        while(node != None):
            if node.val not in self.visited:
                self.visited.append(node.val)
              #  print(self.visited)
                result = self.dfs(node.val,val)
                if result == True:
                    return True
            node = node.next
        return False


        


graph  = Graph()
graph.push(1,[2,3,6])
graph.push(2,[5,1])
graph.push(3,[1,6])
graph.push(4,[5])
graph.push(5,[2,4])
graph.push(6,[1,3])

print(graph.dfsSearch(1,4))
