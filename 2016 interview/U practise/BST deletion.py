#Round3
#BST insertion and deletion

class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left
    
    def insert(self, item):
        if self.data:
            if self.data > item:
                if self.left == None:
                    self.left = Node(item)
                elif self.left != None:
                    self.left.insert(item)
            elif self.data < item:
                if self.right == None:
                    self.right = Node(item)
                elif self.right != None:
                    self.right.insert(item)
        else:
            self.data = item


def children_count(self):
    
    count = 0
        
        if self.left:
            count += 1
    if self.right:
        count += 1
        
        return count

    #find delete node and its parent, can also be done in insertion
    def lookup(self, data, parent=None):
        
        if self.data == data:
            return self, parent
        if data < self.data:
            if self.left is None:
                return None
            else:
                return self.left.lookup(data, parent=self)
        else:
            if self.right is None:
                return None
            else:
                return self.right.lookup(data, parent=self)

def delete(self, data):
    node, parent = self.lookup(data)
        #the node with no children
        if node.children_count() == 0:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            del node

    #the node with one children
    elif node.children_count() == 1:
        if node.left:
            n = node.left
            else:
                n = node.right
        if parent:
            if parent.left == node:
                parent.left = n
                else:
                    parent.right = n
del node
    
    #the node with two children
    else:
        # find the successor
        parent = node
            successor = node.right
            
            while successor.left:
                parent = successor
                successor = successor.left
        print parent.data, successor.data
            #node replace the data with successor
            #and attach the successor right branch to successor's parent
            #    -> because the successor guarantee with no left branch
            node.data = successor.data
            if parent.left == successor:
                parent.left = successor.right
        else:
            parent.right = successor.right


def printN(root):
    if root == None:
        return
    printN(root.left)
    print root.data
    printN(root.right)


#1, pre-order traverse
def list_depth(root, mLists, level):
    #the root is None
    if root == None:
        return
    
    #the level not exist, master list only reach level-1 sublists
    # len(mLists) <= level: easier to think, need more sublist to cover the level
    if len(mLists) == level:
        mLists.append([root.data])
    else:
        mLists[level].extend([root.data])
    
    list_depth(root.left, mLists, level+1)
    list_depth(root.right, mLists, level+1)

root = Node(42)
root.insert(45)
root.insert(25)
root.insert(12)
root.insert(37)
root.insert(9)
root.insert(13)
root.insert(30)
root.insert(40)
#printN(root)
#print by level
mLists = []
list_depth(root, mLists, 0)
print mLists
mLists = []


root.delete(25)
list_depth(root, mLists, 0)
print mLists
