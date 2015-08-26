#build up the BST
class Node(object):
    def __init__(self, data, parent = None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        
        
    def insert(self, data):
        #check the root data first
        if self.data:
            #check the right hand side
            if(self.data > data):
                if self.left is None:
                    self.left = Node(data, self)
                else:
                    self.left.insert(data)
            elif(self.data < data):
                if self.right is None:
                    self.right = Node(data, self)
                else:
                    self.right.insert(data)
        else:
            self.data = data

#building the BST
root = Node(42, None)
root.insert(45)
root.insert(25)
root.insert(12)
root.insert(37)
root.insert(9)
root.insert(13)
root.insert(40)