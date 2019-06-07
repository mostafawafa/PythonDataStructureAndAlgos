


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None



class BinarySearchTreeCollection:
    
    def construct_bst(self,arr):
        root = TreeNode(arr[0])
        for item in arr:
            node = TreeNode(item)
            self.add_node(root,node)
        return root

    def add_node(self,root,node):
        if(root.val > node.val):
            if( not root.left):
                root.left = node
            else:
                self.add_node(root.left,node)
        if(root.val < node.val):
            if( not root.right):
                root.right = node
            else:
                self.add_node(root.right,node)

    def pre_order(self,root):
        if not root:
            return 
        self.visit(root)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self,root):
        if not root:
            return
        self.in_order(root.left)
        self.visit(root)
        self.in_order(root.right)

    def visit(self,item):
        print(item.val)

    def post_order(self,root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        self.visit(root)

    def construct_from_sorted(self,array):
        length = len(array)
        mid = (length // 2 )
        root = TreeNode(array[mid])
        root.left = self.construct_from_sorted_helper(array[:mid])
        root.right = self.construct_from_sorted_helper(array[(mid+1):])
        return root

    def construct_from_sorted_helper(self,array):
        if not array:
            return None
        length = len(array)
        if length  ==1:
            return TreeNode(array[0])
        mid = (length // 2 ) -1
        print(array,array[mid])

        root = TreeNode(array[mid])
        root.left = self.construct_from_sorted_helper(array[:mid])
        root.right = self.construct_from_sorted_helper(array[mid+1:])
        return root


if __name__ == "__main__":
    
    arr = [4,5,1,6,7]
    tree =  BinarySearchTreeCollection()
    root = tree.construct_bst(arr)
    print(tree.in_order(root))


    root = tree.construct_from_sorted([1,2,3,4,5,6,7,8,9])
    print(tree.post_order(root))

    