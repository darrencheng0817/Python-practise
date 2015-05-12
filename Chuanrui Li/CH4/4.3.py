#Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (i.e., if you have a tree with depth D, you’ll have D linked lists).

#1,) read the array from mid, even -> odd + 1
#2,) insert the data into the BST


array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



#why this part does not work       
#def insert(array, begin, end, node):
    #mid = (begin + end)/2
    #if mid == begin:
        #return
    #else:
        #node = Node(array[mid])
        #insert(array, begin, mid, node.left)
        #insert(array, mid, end, node.right)
        
#root = Node(9)
#insert(array, 0, 8, root)	
#print root.left


def insert(array, begin, end):
    mid = (begin + end)/2
    if mid == 0:
        return Node(array[0])
    elif mid == len(array)-2 and mid == begin:
        print "hehe"
        return Node(array[-1])
    elif mid == begin:
        return 
    else:
        node = Node(array[mid])
        node.left = insert(array, begin, mid)
        node.right = insert(array, mid, end)
        return node
#postorder print left, right, root
def printn(root):
    if root == None:
        return
    printn(root.left)
    printn(root.right)
    print root.data

root = Node(9)
node = insert(array, 0, 8)	
printn(node)



    