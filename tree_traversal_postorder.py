# Tree with post-order traversal

class Node:

    '''
        Used to create a copy/replica of the tree

        Usage:
            root = Node(50)
            root.insert(30)
            root.insert(70)
            root.insert(20)
            root.insert(40)
            root.insert(60)
            root.insert(80)
            root.printer()
            root.traversalPostorder(root)
        Output:
            20 30 40 50 60 70 80 
            [20, 40, 30, 60, 80, 70, 50]
        Order of traversal:
            root.left.left.left, \
            root.left.left.right, \
            root.left.left.root, \
            root.left.right.left, \
            root.left.right.right, \
            root.left.right.root, \
            root.left.root, \
            root.right.left.left, \
            root.right.left.right, \
            root.right.left.root, \
            root.right.right.left, \
            root.right.right.right, \
            root.right.right.root, \
            root.right.root, \
            root.root
    '''
    
    def __init__(self, element):
        
        self.root = element
        self.left = None
        self.right = None
        self.counter = 0
        
    def insert(self, element):
        
        if self.root:
            
            if element < self.root:
                
                if self.left:
                    self.left.insert(element)
                else:
                    self.left = Node(element)
                
            if element > self.root:
                
                if self.right:
                    self.right.insert(element)
                else:
                    self.right = Node(element)
                
        else:
            self.root = element
            
    def printer(self):
        
        if self.left:
            self.left.printer()
        print(self.root, end=" ")
        if self.right:
            self.right.printer()
            
    def traversalPostorder(self, data):
        self.counter += 1
#         print(self.counter)
        
        element_list = []
        
        if data:
            element_list = self.traversalPostorder(data.left)
            element_list = element_list + self.traversalPostorder(data.right)
            element_list.append(data.root)
            
        return element_list
