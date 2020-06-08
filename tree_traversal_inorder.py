# Tree with in-order traversal

class Node:

    '''
        Used to get elements based on an ascending order in a tree

        Usage:
            root = Node(50)
            root.insert(30)
            root.insert(70)
            root.insert(20)
            root.insert(40)
            root.insert(60)
            root.insert(80)
            root.printer()
            root.traversalInorder(root)
        Output:
            20 30 40 50 60 70 80 
            [20, 30, 40, 50, 60, 70, 80]
        Order of traversal:
            root.left.left.left, \
            root.left.left.root, \
            root.left.left.right, \
            root.left.root, \
            root.left.right.left, \
            root.left.right.right, \
            root.left.right.root, \
            root.root, \
            root.right.left.left, \
            root.right.left.root, \
            root.right.left.right, \
            root.right.root, \
            root.right.right.left, \
            root.right.right.root, \
            root.right.right.right
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
            
    def traversalInorder(self, data):
        self.counter += 1
#         print(self.counter)
        
        element_list = []
        
        if data:
            element_list = self.traversalInorder(data.left)
            element_list.append(data.root)
            element_list = element_list + self.traversalInorder(data.right)
        
        return element_list
